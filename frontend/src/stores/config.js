import { defineStore } from "pinia";
import { TOKEN_STORE, USER_STORE } from "../constantes";

export const useConfigStore = defineStore({
  id: "configs",
  state: () => ({
    actionBar: false,
  }),
  getters: {
    isActionBar: (store) => {
      return store.actionBar;
    },
  },
  actions: {
    setActionBar(payload) {
      this.actionBar = payload;
    },
  },
});
