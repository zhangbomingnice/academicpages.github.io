#!/usr/bin/env python3
"""
Fetch country-level analytics from Umami and write them to a static JSON file
consumed by the footer visitor map on the Jekyll site.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

import pycountry
import requests


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = REPO_ROOT / "assets" / "data" / "visitor-map-live.json"
DEFAULT_API_BASE_URL = "https://api.umami.is/v1"
DEFAULT_START_AT = "2000-01-01T00:00:00Z"

COUNTRY_ALIASES = {
    "bolivia": "BO",
    "czechia": "CZ",
    "iran": "IR",
    "kosovo": "XK",
    "laos": "LA",
    "moldova": "MD",
    "north korea": "KP",
    "russia": "RU",
    "south korea": "KR",
    "syria": "SY",
    "taiwan": "TW",
    "tanzania": "TZ",
    "venezuela": "VE",
    "vietnam": "VN",
}


def getenv(name: str, default: str | None = None, required: bool = False) -> str:
    value = os.getenv(name, default)
    if value == "":
        value = default
    if required and not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value or ""


def parse_datetime_to_ms(value: str) -> int:
    normalized = value.strip()
    if normalized.isdigit():
        return int(normalized)
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp() * 1000)


def build_url(base_url: str, path: str) -> str:
    prefix = base_url.rstrip("/") + "/"
    return urljoin(prefix, path.lstrip("/"))


def build_headers(api_base_url: str) -> dict[str, str]:
    api_key = getenv("UMAMI_API_KEY")
    if api_key:
        return {
            "Accept": "application/json",
            "x-umami-api-key": api_key,
        }

    username = getenv("UMAMI_USERNAME")
    password = getenv("UMAMI_PASSWORD")
    if not username or not password:
        raise RuntimeError(
            "Provide either UMAMI_API_KEY, or UMAMI_USERNAME + UMAMI_PASSWORD."
        )

    response = requests.post(
        build_url(api_base_url, "/auth/login"),
        json={"username": username, "password": password},
        headers={"Accept": "application/json"},
        timeout=60,
    )
    response.raise_for_status()
    payload = response.json()
    token = payload.get("token")
    if not token:
        raise RuntimeError("Umami login succeeded but no token was returned.")

    return {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    }


def umami_get(api_base_url: str, path: str, headers: dict[str, str], params: dict) -> object:
    response = requests.get(
        build_url(api_base_url, path),
        headers=headers,
        params=params,
        timeout=60,
    )
    response.raise_for_status()
    return response.json()


def normalize_summary(data: object) -> dict:
    if not isinstance(data, dict):
        raise RuntimeError("Unexpected Umami summary response format")

    return {
        "pageviews": int(data.get("pageviews") or 0),
        "visitors": int(data.get("visitors") or 0),
    }


def country_name_to_code(name: str) -> str:
    normalized = name.strip()
    if not normalized:
        return ""

    alias_code = COUNTRY_ALIASES.get(normalized.casefold())
    if alias_code:
        return alias_code

    try:
        return pycountry.countries.lookup(normalized).alpha_2
    except LookupError:
        return ""


def normalize_countries(data: object) -> list[dict]:
    if not isinstance(data, list):
        raise RuntimeError("Unexpected Umami country response format")

    countries: list[dict] = []
    for row in data:
        if not isinstance(row, dict):
            continue

        name = str(row.get("name") or row.get("x") or "").strip()
        if not name or name.lower() == "unknown":
            continue

        code = country_name_to_code(name)
        if not code:
            continue

        value = int(row.get("visits") or row.get("pageviews") or row.get("visitors") or row.get("y") or 0)
        if value <= 0:
            continue

        countries.append(
            {
                "code": code,
                "name": name,
                "display_name": name,
                "value": value,
            }
        )

    countries.sort(key=lambda item: item["value"], reverse=True)
    return countries


def build_payload(summary: dict, countries: list[dict]) -> dict:
    updated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return {
        "status_label": "实时数据",
        "summary": {
            "pageviews": summary["pageviews"],
            "visitors": summary["visitors"],
            "countries": len(countries),
            "updated_at": updated_at,
            "source_label": "Umami 新增访问",
            "source_detail": "当前显示会把历史基线与你之后的真实访客新增量相加；国家热力图按 Umami 的真实国家统计同步。",
        },
        "countries": countries,
    }


def main() -> int:
    try:
        api_base_url = getenv("UMAMI_API_BASE_URL", DEFAULT_API_BASE_URL)
        website_id = getenv("UMAMI_WEBSITE_ID", required=True)
        start_at = parse_datetime_to_ms(getenv("UMAMI_START_AT", DEFAULT_START_AT))
        end_at = parse_datetime_to_ms(getenv("UMAMI_END_AT", datetime.now(timezone.utc).isoformat()))
        headers = build_headers(api_base_url)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    params = {
        "startAt": start_at,
        "endAt": end_at,
    }

    try:
        summary_data = umami_get(
            api_base_url,
            f"/websites/{website_id}/stats",
            headers,
            params,
        )
        country_data = umami_get(
            api_base_url,
            f"/websites/{website_id}/metrics/expanded",
            headers,
            {
                **params,
                "type": "country",
                "limit": 500,
            },
        )
    except requests.RequestException as exc:
        print(f"Failed to fetch Umami data: {exc}", file=sys.stderr)
        return 1

    try:
        summary = normalize_summary(summary_data)
        countries = normalize_countries(country_data)
        payload = build_payload(summary, countries)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote visitor map data to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
