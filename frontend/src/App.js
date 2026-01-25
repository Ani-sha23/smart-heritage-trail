import React, { useEffect, useState } from "react";
import { getCities, getSites } from "./api";

function App() {
  const [state] = useState("Madhya Pradesh");
  const [cities, setCities] = useState([]);
  const [city, setCity] = useState("");
  const [sites, setSites] = useState([]);

  // Load cities when app loads
  useEffect(() => {
    getCities(state)
      .then((res) => {
        console.log("Cities:", res.data); // DEBUG
        setCities(res.data);
      })
      .catch((err) => console.error("City error:", err));
  }, [state]);

  // Load sites when button clicked
  const loadSites = () => {
    if (!city) {
      alert("Please select a city");
      return;
    }

    getSites(state, city)
      .then((res) => setSites(res.data))
      .catch((err) => console.error("Sites error:", err));
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Smart Heritage Trail – MP</h1>

      <p><b>State:</b> {state}</p>

      <label>
        <b>City:</b>{" "}
        <select value={city} onChange={(e) => setCity(e.target.value)}>
          <option value="">Select City</option>
          {cities.map((c, i) => (
            <option key={i} value={c}>
              {c}
            </option>
          ))}
        </select>
      </label>

      <br /><br />

      <button onClick={loadSites}>Generate Heritage Trail</button>

      <br /><br />

      {sites.length > 0 && (
        <>
          <h3>Heritage Sites</h3>
          <ul>
            {sites.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}

export default App;
