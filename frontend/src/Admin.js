import { useEffect, useState } from "react";
import { getAllSites, addSite, deleteSite } from "./adminApi";

function Admin() {
  const [sites, setSites] = useState([]);
  const [form, setForm] = useState({
    name: "",
    category: "",
    city: "",
    state: "",
  });

  const loadSites = () => {
    getAllSites().then(setSites);
  };

  useEffect(() => {
    loadSites();
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    addSite(form).then(() => {
      setForm({ name: "", category: "", city: "", state: "" });
      loadSites();
    });
  };

  return (
    <div className="container">
      <h1>🛠 Admin Dashboard</h1>

      <h3>Add Heritage Site</h3>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Site Name"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
        />
        <input
          placeholder="Category (Fort/Museum/etc)"
          value={form.category}
          onChange={(e) => setForm({ ...form, category: e.target.value })}
        />
        <input
          placeholder="City"
          value={form.city}
          onChange={(e) => setForm({ ...form, city: e.target.value })}
        />
        <input
          placeholder="State"
          value={form.state}
          onChange={(e) => setForm({ ...form, state: e.target.value })}
        />
        <button type="submit">Add Site</button>
      </form>

      <h3>All Heritage Sites</h3>
      <ul>
        {sites.map((s) => (
          <li key={s.id}>
            {s.name} ({s.category}) — {s.city}, {s.state}
            <button onClick={() => deleteSite(s.id).then(loadSites)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Admin;
