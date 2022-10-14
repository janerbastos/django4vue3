<script setup>
import Navbar from "./components/layout/Navbar.vue";
import Sidebar from "./components/layout/Sidebar.vue";
import ContentHeader from "./components/layout/ContentHeader.vue";
import ControlSidebar from "./components/layout/ControlSidebar.vue";
import Footer from "./components/layout/Footer.vue";
</script>

<template>
  <div>
    <navbar />
    <sidebar />
    <content-header />
    <control-sidebar />
    <Footer />
  </div>
</template>

<style scoped>
</style>
