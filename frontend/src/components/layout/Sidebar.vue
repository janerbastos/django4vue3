<script setup>
import { HOST_IMG } from "../../constantes";
import Nav from "../menu/Nav.vue";
import NavItem from "../menu/NavItem.vue";
import NavTreeview from "../menu/NavTreeview.vue";
</script>
<template>
  <!-- Main Sidebar Container -->
  <aside class="main-sidebar sidebar-dark-primary elevation-4">
    <!-- Brand Logo -->
    <a href="/" class="brand-link">
      <img
        :src="HOST_IMG + 'AdminLTELogo.png'"
        alt="AdminLTE Logo"
        class="brand-image img-circle elevation-3"
        style="opacity: 0.8"
      />
      <span class="brand-text font-weight-light">AdminLTE 2</span>
    </a>

    <!-- Sidebar -->
    <div class="sidebar">
      <!-- Sidebar user panel (optional) -->
      <div class="user-panel mt-3 pb-3 mb-3 d-flex">
        <div class="image">
          <img
            :src="HOST_IMG + 'user2-160x160.jpg'"
            class="img-circle elevation-2"
            alt="User Image"
          />
        </div>
        <div class="info">
          <a href="#" class="d-block"> Janer </a>
        </div>
      </div>

      <!-- SidebarSearch Form -->
      <div class="form-inline">
        <div class="input-group" data-widget="sidebar-search">
          <input
            class="form-control form-control-sidebar"
            type="search"
            placeholder="Search"
            aria-label="Search"
          />
          <div class="input-group-append">
            <button class="btn btn-sidebar">
              <i class="fas fa-search fa-fw"></i>
            </button>
          </div>
        </div>
      </div>

      <!-- Sidebar Menu -->
      <Nav>
        <NavItem
          titulo="Configure"
          :active="false"
          :open="true"
          icon="fa-tasks"
        >
          <nav-treeview>
            <li class="nav-item">
              <router-link to="/users" class="nav-link">
                <i class="fas fa-users nav-icon"></i>
                <p>Usuários</p>
              </router-link>
            </li>
          </nav-treeview>
        </NavItem>
      </Nav>
      <!--<nav class="mt-2">
        <ul
          class="nav nav-pills nav-sidebar flex-column"
          data-widget="treeview"
          role="menu"
          data-accordion="false"
        >
          <li class="nav-item">
            <router-link to="/users" class="nav-link">
              <i class="nav-icon fas fa-users"></i>
              <p>
                Usuarios
                <span class="right badge badge-danger">New</span>
              </p>
            </router-link>
          </li>
        </ul>
      </nav> -->
      <!-- /.sidebar-menu -->
    </div>
    <!-- /.sidebar -->
  </aside>
</template>