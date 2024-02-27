<template>
  <!-- Content Wrapper. Contains page content -->
  <div class="content-wrapper">
    <Header titulo="Usuarios" />
    <!-- Main content -->
    <div class="content">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12">
            <div class="card">
              <div class="card-body table-responsive p-0">
                <table class="table table-hover text-nowrap">
                  <thead>
                    <tr>
                      <th>ID</th>
                      <th>Nome</th>
                      <th>Data de registro</th>
                      <th>Status</th>
                      <th>Papel</th>
                      <th>Administrador</th>
                      <td></td>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="usuario in usuarios" :key="usuario.id">
                      <td>{{ usuario.id }}</td>
                      <td>{{ usuario.first_name }}</td>
                      <td>{{ data(usuario.date_joined) }}</td>
                      <td>
                        <span class="tag tag-success">
                          {{ usuario.is_active ? "Ativo" : "Bloqueado" }}
                        </span>
                      </td>
                      <td>
                        <span class="tag tag-success">
                          {{ usuario.is_admin ? "Gestor" : "-" }}
                        </span>
                      </td>
                      <td>
                        <span
                          class="tag tag-success text-success"
                          v-html="iconIsAdmin(usuario.is_superadmin)"
                        >
                        </span>
                      </td>
                      <td>
                        <span class="text-primary">
                          <router-link
                            :to="{
                              name: 'EditUser',
                              params: { id: usuario.id },
                            }"
                          >
                            <i class="fas fa-user-edit"></i>
                          </router-link>
                        </span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
        <!-- /.row -->
      </div>
      <!-- /.container-fluid -->
    </div>
    <!-- /.content -->
  </div>
  <!-- /.content-wrapper -->
</template>

<script setup>
import { BASE_SITE } from "../../../constantes";
import { ref, onMounted } from "vue";
import Header from "../../layout/Header.vue";
import axios from "axios";
import moment from "moment";

const usuarios = ref([]);
const API = BASE_SITE + "usuarios/apis/v1/";

const loadUsuarios = () => {
  axios.get(`${API}users/`).then((resp) => {
    usuarios.value = resp.data;
    console.log(usuarios.value);
  });
};

const data = (value) => {
  return moment(value).format("DD/MM/YYYY, h:mm:ss");
};

const iconIsAdmin = (value) => {
  if (value) {
    return "<i class='fas fa-check-circle'></i>";
  }
  return "-";
};

onMounted(() => {
  loadUsuarios();
});
</script>

<style>
</style>