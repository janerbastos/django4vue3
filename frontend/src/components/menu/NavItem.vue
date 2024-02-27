<template>
  <li class="nav-item" :class="{ 'menu-open': isOpen }">
    <a href="#" class="nav-link" :class="{ active: active }" @click="openMenu">
      <i class="nav-icon fas" :class="icon"></i>
      <p>
        {{ titulo }}
        <i class="right fas fa-angle-left"></i>
      </p>
    </a>
    <slot />
  </li>
</template>

<script setup>
import { ref } from "vue";

const isOpen = ref(props.open);

const openMenu = () => {
  isOpen.value = !isOpen.value;
};

const props = defineProps({
  open: {
    type: Boolean,
    default: false,
  },
  active: {
    type: Boolean,
    default: false,
  },
  titulo: {
    type: String,
    required: true,
  },
  icon: {
    type: String,
    default: "fa-thermometer",
  },
});
</script>

<style>
</style>