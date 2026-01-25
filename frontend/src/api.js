import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const getCities = (state) =>
  API.get(`/cities/${state}`);

export const getSites = (state, city) =>
  API.get(`/sites/${state}/${city}`);
