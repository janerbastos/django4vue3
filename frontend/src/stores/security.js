import { defineStore } from "pinia";
import { TOKEN_STORE, USER_STORE } from "../constantes";

export const useSecurityStore = defineStore({
  id: "securitys",
  state: () => ({
    user: {},
    isAuthenticated: false,
    token: "",
  }),
  getters: {
    inicializeStore: (state) => {
      const accessToken = localStorage.getItem(TOKEN_STORE);
      const user_register = localStorage.getItem(USER_STORE);
      if (accessToken) {
        state.token = JSON.parse(accessToken);
        state.user = JSON.parse(user_register);
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
        state.user = {};
      }
      return state.user;
    },

    getUser: (state) => state.user,
  },
  actions: {
    setUser(payload) {
      this.user = payload;
    },
    setIsAuthenticated(payload) {
      this.isAuthenticated = payload;
    },
    logout() {
      this.token = undefined;
      this.isAuthenticated = false;
      this.user = {};
      localStorage.removeItem(TOKEN_STORE);
      localStorage.removeItem(USER_STORE);
    },
  },
});
