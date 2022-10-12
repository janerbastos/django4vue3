import axios from "axios";
import { BASE_URL, TOKEN_STORE, USER_STORE } from "../constantes";

axios.defaults.baseURL = BASE_URL;
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status === 401) {
      localStorage.removeItem(TOKEN_STORE);
      localStorage.removeItem(USER_STORE);
      window.location.replace("/nao-autorizado");
    }
    return Promise.reject(error);
  }
);

export { axios };
