import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/HomePage.vue";
import Login from "../components/LoginPage.vue";
import "bootstrap/dist/css/bootstrap.css";

const routes = [
  {
    path: "/home",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
