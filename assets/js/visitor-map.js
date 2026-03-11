(function () {
  function formatNumber(value) {
    var number = Number(value || 0);
    return number.toLocaleString("zh-CN");
  }

  function updateText(selector, value, formatter) {
    var element = document.querySelector(selector);
    if (!element || value === undefined || value === null || value === "") {
      return;
    }

    element.textContent = formatter ? formatter(value) : value;
  }

  function renderHotspots(countries) {
    var list = document.querySelector("[data-visitor-map-hotspots]");
    if (!list) {
      return;
    }

    var topCountries = countries
      .slice()
      .sort(function (a, b) {
        return (Number(b.value) || 0) - (Number(a.value) || 0);
      })
      .slice(0, 5);

    list.innerHTML = topCountries
      .map(function (item) {
        var label = item.display_name || item.name;
        return "<li>" + label + " · " + formatNumber(item.value) + "</li>";
      })
      .join("");
  }

  function buildOption(payload) {
    var countries = Array.isArray(payload.countries) ? payload.countries : [];
    var values = countries
      .map(function (item) {
        return Number(item.value) || 0;
      })
      .filter(function (value) {
        return value > 0;
      });
    var max = values.length ? Math.max.apply(null, values) : 100;

    return {
      tooltip: {
        trigger: "item",
        formatter: function (params) {
          var value = params.value || 0;
          var label = params.data && params.data.display_name ? params.data.display_name : params.name;
          return label + "<br/>访问次数: " + formatNumber(value);
        }
      },
      visualMap: {
        min: 0,
        max: max,
        orient: "horizontal",
        left: "center",
        bottom: 4,
        text: ["高", "低"],
        calculable: false,
        itemWidth: 140,
        itemHeight: 10,
        textStyle: {
          color: "#5b6472"
        },
        inRange: {
          color: ["#dfe4ea", "#c7d2fe", "#93c5fd", "#60a5fa", "#2563eb"]
        }
      },
      series: [
        {
          type: "map",
          map: "world",
          roam: true,
          nameProperty: "name",
          emphasis: {
            label: {
              show: false
            },
            itemStyle: {
              areaColor: "#f59e0b"
            }
          },
          itemStyle: {
            areaColor: "#eceff3",
            borderColor: "#ffffff",
            borderWidth: 0.7
          },
          data: countries
        }
      ]
    };
  }

  function normalizePayload(rawPayload) {
    var payload = rawPayload || {};
    var summary = payload.summary || {};
    var countries = Array.isArray(payload.countries) ? payload.countries : [];

    return {
      mode: payload.mode || "demo",
      status_label: payload.status_label || (payload.mode === "live" ? "实时数据" : "演示预览"),
      endpoint: payload.endpoint || "",
      summary: {
        pageviews: summary.pageviews || 0,
        visitors: summary.visitors || 0,
        countries: summary.countries || countries.length,
        updated_at: summary.updated_at || "",
        source_label: summary.source_label || "",
        source_detail: summary.source_detail || ""
      },
      countries: countries
    };
  }

  function mergePayload(basePayload, remotePayload) {
    var merged = Object.assign({}, basePayload, remotePayload);
    merged.summary = Object.assign({}, basePayload.summary || {}, remotePayload.summary || {});
    merged.countries = Array.isArray(remotePayload.countries) ? remotePayload.countries : basePayload.countries;
    return normalizePayload(merged);
  }

  function buildEndpointUrl(endpoint) {
    if (!endpoint) {
      return "";
    }

    if (/^https?:\/\//.test(endpoint)) {
      return endpoint;
    }

    var root = document.querySelector("[data-visitor-map-root]");
    var baseUrl = root ? root.getAttribute("data-baseurl") || "" : "";
    return baseUrl + endpoint;
  }

  function updateSummary(payload) {
    updateText("[data-visitor-stat='pageviews']", payload.summary.pageviews, formatNumber);
    updateText("[data-visitor-stat='visitors']", payload.summary.visitors, formatNumber);
    updateText("[data-visitor-stat='countries']", payload.summary.countries, formatNumber);
    updateText("[data-visitor-stat='updated_at']", payload.summary.updated_at);
    updateText("[data-visitor-map-source]", payload.summary.source_label);
    updateText("[data-visitor-map-detail]", payload.summary.source_detail);
    updateText("[data-visitor-map-badge]", payload.status_label);
    renderHotspots(payload.countries);
  }

  function renderMap(payload) {
    var chartElement = document.getElementById("visitor-map-chart");
    if (!chartElement || !window.echarts) {
      return;
    }

    var chart = window.echarts.getInstanceByDom(chartElement) || window.echarts.init(chartElement);
    chart.setOption(buildOption(payload));
    window.addEventListener("resize", function () {
      chart.resize();
    });
  }

  function loadPayload(initialPayload) {
    var payload = normalizePayload(initialPayload);
    var endpointUrl = buildEndpointUrl(payload.endpoint);

    if (payload.mode !== "live" || !endpointUrl) {
      return Promise.resolve(payload);
    }

    return fetch(endpointUrl, {
      headers: {
        Accept: "application/json"
      }
    })
      .then(function (response) {
        if (!response.ok) {
          throw new Error("Failed to load visitor map data");
        }
        return response.json();
      })
      .then(function (remotePayload) {
        return mergePayload(payload, remotePayload);
      })
      .catch(function () {
        return payload;
      });
  }

  function init() {
    var payloadNode = document.getElementById("visitor-map-data");
    if (!payloadNode) {
      return;
    }

    try {
      var rawPayload = JSON.parse(payloadNode.textContent);
      loadPayload(rawPayload).then(function (payload) {
        updateSummary(payload);
        renderMap(payload);
      });
    } catch (error) {
      console.error("Visitor map init failed:", error);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
