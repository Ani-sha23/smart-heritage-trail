import { useEffect, useState } from "react";
import {
  getStates,
  getCities,
  generateTrail,
  createPass,
} from "./api";

const INTERESTS = ["Fort", "Museum", "Nature", "Architecture"];

function App() {
  const [states, setStates] = useState([]);
  const [cities, setCities] = useState([]);
  const [selectedState, setSelectedState] = useState("");
  const [selectedCity, setSelectedCity] = useState("");
  const [interests, setInterests] = useState([]);
  const [trail, setTrail] = useState(null);
  const [passData, setPassData] = useState(null);

  // Load states on app load
  useEffect(() => {
    getStates().then(setStates);
  }, []);

  // Toggle interests
  const toggleInterest = (interest) => {
    setInterests((prev) =>
      prev.includes(interest)
        ? prev.filter((i) => i !== interest)
        : [...prev, interest]
    );
  };

  // When state changes
  const handleStateChange = (e) => {
    const state = e.target.value;
    setSelectedState(state);
    setSelectedCity("");
    setCities([]);
    setTrail(null);
    setPassData(null);

    if (state) {
      getCities(state).then(setCities);
    }
  };

  // Generate trail
  const handleGenerateTrail = () => {
    if (!selectedCity) {
      alert("Please select a city");
      return;
    }
    generateTrail(selectedCity, interests).then((data) => {
      setTrail(data);
      setPassData(null);
    });
  };

  // Create digital pass
  const handleCreatePass = () => {
    if (!trail) return;
    createPass(trail).then(setPassData);
  };

  return (
    <div className="container">
      <h1>🏛 Smart Heritage Trail</h1>
      <p>Explore cultural heritage of Madhya Pradesh & Rajasthan</p>

      {/* State Selection */}
      <select value={selectedState} onChange={handleStateChange}>
        <option value="">Select State</option>
        {states.map((state, i) => (
          <option key={i} value={state}>
            {state}
          </option>
        ))}
      </select>

      {/* City Selection */}
      {cities.length > 0 && (
        <select
          value={selectedCity}
          onChange={(e) => setSelectedCity(e.target.value)}
        >
          <option value="">Select City</option>
          {cities.map((city, i) => (
            <option key={i} value={city}>
              {city}
            </option>
          ))}
        </select>
      )}

      {/* Interest Selection */}
      <h3>Interests</h3>
      <div style={{ marginBottom: "10px" }}>
        {INTERESTS.map((interest) => (
          <label key={interest} style={{ marginRight: "15px" }}>
            <input
              type="checkbox"
              checked={interests.includes(interest)}
              onChange={() => toggleInterest(interest)}
            />
            {" "}{interest}
          </label>
        ))}
      </div>

      {/* Generate Trail */}
      <button onClick={handleGenerateTrail}>
        Generate Trail
      </button>

      {/* Trail Output */}
      {trail && (
        <div style={{ marginTop: "20px" }}>
          <h3>Generated Trail – {trail.city}</h3>

          {trail.sites.length === 0 ? (
            <p>No heritage sites match selected interests.</p>
          ) : (
            <ul>
              {trail.sites.map((site, i) => (
                <li key={i}>
                  {site.name} ({site.category})
                </li>
              ))}
            </ul>
          )}

          {trail.sites.length > 0 && (
            <button onClick={handleCreatePass}>
              Create Digital Pass
            </button>
          )}
        </div>
      )}

      {/* Digital Pass */}
      {passData && (
        <div style={{ marginTop: "20px" }}>
          <h3>🎫 Digital Pass</h3>
          <img
            src={`http://127.0.0.1:8000${passData.qr_image}`}
            alt="QR Code"
            width="200"
          />
          <p>Scan QR to view trail details</p>
        </div>
      )}
    </div>
  );
}

export default App;
