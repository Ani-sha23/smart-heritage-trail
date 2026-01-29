const BASE_URL = "http://127.0.0.1:8000";

export async function getStates() {
  const res = await fetch(`${BASE_URL}/states`);
  return res.json();
}

export async function getCities(state) {
  const res = await fetch(`${BASE_URL}/cities/${state}`);
  return res.json();
}

export async function generateTrail(city, interests) {
  const res = await fetch(`${BASE_URL}/generate-trail/${city}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(interests),
  });
  return res.json();
}

export async function createPass(trail) {
  const res = await fetch(`${BASE_URL}/create-pass`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(trail),
  });
  return res.json();
}
