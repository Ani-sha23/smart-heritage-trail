import React, { useEffect, useState } from "react";
import "./App.css";
import { getCities, getSites } from "./api";

function App() {
  const state = "Madhya Pradesh";

  const [cities, setCities] = useState([]);
  const [city, setCity] = useState("");
  const [sites, setSites] = useState([]);
  const [error, setError] = useState("");

  // Load cities on page load
  useEffect(() => {
    getCities(state)
      .then((res) => {
        setCities(res.data);
        setError("");
      })
      .catch(() => {
        setError("Failed to load cities");
      });
  }, []);

  // Load heritage sites
  const loadSites = () => {
    if (!city) return;

    getSites(state, city)
      .then((res) => {
        setSites(res.data);
        setError("");
      })
      .catch(() => {
        setError("Failed to load heritage sites");
        setSites([]);
      });
  };

  return (
    <div className="container">
      <h1>Smart Heritage Trail</h1>
      <p className="subtitle">
        Discover cultural heritage sites city-wise
      </p>

      <div className="state-line">
        <span className="state-label">State:</span>
        <span className="state-value">Madhya Pradesh</span>
      </div>


      <div className="form-group">
        <select value={city} onChange={(e) => setCity(e.target.value)}>
          <option value="">Select City</option>
          {cities.map((c) => (
            <option key={c} value={c}>
              {c}
            </option>
          ))}
        </select>

        <button onClick={loadSites} disabled={!city}>
          Generate Heritage Trail
        </button>
      </div>

      {error && <div className="error">{error}</div>}

      {sites.length > 0 && (
        <div className="results">
          <h2>Heritage Sites</h2>
          <ul>
            {sites.map((s, i) => (
              <li key={i}>
                <div>
                  <b>{s.name}</b>
                  <p style={{ margin: "5px 0", color: "#555" }}>
                    {s.desc}
                  </p>
                </div>
                <a
                  href={`https://www.google.com/maps/search/${encodeURIComponent(
                    s.name + " " + city + " " + state
                  )}`}
                  target="_blank"
                  rel="noreferrer"
                  className="map-link"
                >
                  📍 Map
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
