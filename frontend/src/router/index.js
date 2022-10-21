import { createRouter, createWebHistory } from "vue-router";

import { useSecurityStore } from "../stores/security";
import Users from "../components/pages/Users.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Users",
      component: Users,
    },
    {
      path: "/users",
      name: "Home",
      component: Users,
    },
  ],
});

router.beforeEach((to, from, next) => {
  const security = useSecurityStore();
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !security.isAuthenticated
  ) {
    next("/");
  } else {
    next();
  }
});

export default router;
