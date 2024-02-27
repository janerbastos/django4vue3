import { createApp } from "vue";
import { createPinia } from "pinia";

import "admin-lte/dist/css/adminlte.css";
import "./assets/style.css";
import App from "./App.vue";
import router from "./router";
import { axios } from "./axios/interceptors";

const app = createApp(App);

const pinia = createPinia();

app.use(pinia);
app.use(router, axios);
// app.use(CKEditor);

app.mount("#app");
