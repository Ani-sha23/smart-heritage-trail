<div className="container">
  {/* HEADER */}
  <div className="header">
    <h1>Smart Heritage Trail</h1>
    <p>Discover cultural heritage sites city-wise</p>
  </div>

  {/* STATE INFO */}
  <div className="state-box">
    <span className="badge">📍 State</span>
    <span className="state-name">Madhya Pradesh</span>
  </div>

  {/* CONTROLS */}
  <div className="controls">
    <select value={city} onChange={(e) => setCity(e.target.value)}>
      <option value="">🏙️ Select City</option>
      {cities.map((c) => (
        <option key={c} value={c}>{c}</option>
      ))}
    </select>

    <button onClick={loadSites} disabled={!city}>
      🚀 Generate Trail
    </button>
  </div>

  {/* ERROR */}
  {error && <div className="error">⚠️ {error}</div>}

  {/* RESULTS */}
  {sites.length > 0 && (
    <>
      <h2 className="section-title">🏛️ Heritage Sites</h2>

      <div className="sites-grid">
        {sites.map((s, i) => (
          <div key={i} className="site-card">
            <div>
              <h3>{s.name}</h3>
              <p>{s.desc}</p>
            </div>

            <a
              href={`https://www.google.com/maps/search/${encodeURIComponent(
                s.name + " " + city + " Madhya Pradesh"
              )}`}
              target="_blank"
              rel="noreferrer"
              className="map-link"
            >
              📍 Map
            </a>
          </div>
        ))}
      </div>
    </>
  )}
</div>
