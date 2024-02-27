import { createRouter, createWebHistory } from "vue-router";

import { useSecurityStore } from "../stores/security";
import Users from "../components/pages/users/Users.vue";
import EditUser from "../components/pages/users/EditUser.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Users",
      component: Users,
    },
    {
      path: "/user/:id",
      name: "EditUser",
      component: EditUser,
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
