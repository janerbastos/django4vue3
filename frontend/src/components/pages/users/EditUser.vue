<template>
  <div class="content-wrapper">
    <Header :titulo="usuario.first_name" />
    <!-- Main content -->

    <div class="content">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12">
            <div class="card">
              <div class="card-body">
                <!-- Conteudo aqui -->
                <div class="row">
                  <div class="col-md-6">
                    <div class="form-group">
                      <label for="primeiro-nome">Nome</label>
                      <input
                        type="text"
                        class="form-control"
                        id="primeiro-nome"
                        placeholder="Primeiro nome"
                        v-model="usuario.first_name"
                      />
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="form-group">
                      <label for="ultimo-nome">Ultimo nome</label>
                      <input
                        type="text"
                        class="form-control"
                        id="ultimo-nome"
                        placeholder="ultimo nome"
                        v-model="usuario.last_name"
                      />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-6">
                    <div class="form-group">
                      <label for="email">Email</label>
                      <input
                        type="email"
                        class="form-control"
                        id="email"
                        placeholder="Email"
                        v-model="usuario.email"
                      />
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="form-group">
                      <label for="telefone">Telefone</label>
                      <input
                        type="text"
                        class="form-control"
                        id="telefone"
                        placeholder="Telefone para contato."
                        v-model="usuario.phone_number"
                      />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-12">
                    <button
                      type="button"
                      class="btn btn-success"
                      @click="updateUsuario"
                    >
                      Submeter
                    </button>
                  </div>
                </div>
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
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import Header from "../../layout/Header.vue";
import { BASE_SITE } from "../../../constantes";
import { useConfigStore } from "../../../stores/config";

const config = useConfigStore();
const usuario = ref({});
const API = BASE_SITE + "usuarios/apis/v1/";
const route = useRoute();

const loadUsuario = () => {
  const uid = route.params.id;
  axios.get(`${API}users/${uid}/`).then((resp) => {
    usuario.value = resp.data;
  });
};

const updateUsuario = () => {
  const uid = route.params.id;
  const data = { ...usuario.value };
  axios.patch(`${API}users/${uid}/`, data).then((resp) => {
    usuario.value = resp.data;
    config.openCloseToast(true);
  });
};

onMounted(() => {
  loadUsuario();
});
</script>

<style>
</style>