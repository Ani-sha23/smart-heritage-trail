const BASE_URL = "http://127.0.0.1:8000/admin";

export async function getAllSites() {
  const res = await fetch(`${BASE_URL}/sites`);
  return res.json();
}

export async function addSite(data) {
  const res = await fetch(`${BASE_URL}/add-site`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function deleteSite(id) {
  const res = await fetch(`${BASE_URL}/delete-site/${id}`, {
    method: "DELETE",
  });
  return res.json();
}
