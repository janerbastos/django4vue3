<script setup>
import Navbar from "./components/layout/Navbar.vue";
import Sidebar from "./components/layout/Sidebar.vue";
import ContentHeader from "./components/layout/Content.vue";
import ControlSidebar from "./components/layout/ControlSidebar.vue";
import Footer from "./components/layout/Footer.vue";
import Toast from "./components/Toast.vue";

import { useConfigStore } from "./stores/config";

const config = useConfigStore();
</script>

<template>
  <div class="sidebar-mini" :class="{ 'sidebar-collapse': config.isActionBar }">
    <navbar />
    <sidebar />
    <content-header />
    <control-sidebar />
    <Footer />
    <toast v-if="config.getToast.active" />
  </div>
</template>

<style scoped>
</style>
