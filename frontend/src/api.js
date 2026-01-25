import axios from "axios";

const API = axios.create({
  baseURL: "https://smart-heritage-backend.onrender.com"
});

export const getCities = (state) =>
  API.get(`/cities/${state}`);

export const getSites = (state, city) =>
  API.get(`/sites/${state}/${city}`);
