import { createRouter, createWebHistory } from "vue-router";

import { useSecurityStore } from "../stores/security";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: "/nao-autorizado",
    //   name: "NaoAutorizado",
    //   component: NaoAutorizado,
    // },
  ],
});

router.beforeEach((to, from, next) => {
  const security = useSecurityStore();
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !security.isAuthenticated
  ) {
    next("/nao-autorizado");
  } else {
    next();
  }
});

export default router;
