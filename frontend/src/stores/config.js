import { defineStore } from "pinia";

export const useConfigStore = defineStore({
  id: "configs",
  state: () => ({
    actionBar: false,
    toast: {
      message: "Operação realizada com sucesso",
      color: "toast-success",
      time: 3000,
      active: false,
    },
  }),
  getters: {
    isActionBar: (store) => {
      return store.actionBar;
    },
    getToast: (store) => {
      return store.toast;
    },
  },
  actions: {
    setActionBar(payload) {
      this.actionBar = payload;
    },
    setParamToast(payload) {
      this.toast = payload;
    },
    openCloseToast(payload) {
      this.toast.active = payload;
    },
  },
});
