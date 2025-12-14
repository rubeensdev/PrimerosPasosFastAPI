<template>
  <div v-if="show" class="modal-overlay">
    <div class="modal-content">
      <button class="close-btn" @click="$emit('close')">X</button>

      <form @submit.prevent="crear">
        <h3>Crear nueva película</h3>

        <label>Título</label>
        <input type="text" v-model="nuevaPelicula.titulo" placeholder="Título" required /><br><br>

        <label>Género</label>
        <input type="text" v-model="nuevaPelicula.genero" placeholder="Género" required /><br><br>

        <label>Año</label>
        <input type="number" v-model="nuevaPelicula.ano" placeholder="Año" required /><br><br>

        <input type="submit" value="Crear">
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CrearPelicula',
  props: { show: Boolean },
  data() {
    return {
      nuevaPelicula: {
        titulo: '',
        genero: '',
        ano: ''
      }
    }
  },
  methods: {
    crear() {
      this.$emit('crear', { ...this.nuevaPelicula })
      this.nuevaPelicula = { titulo: '', genero: '', ano: '' }
      this.$emit('close')
    }
  }
}
</script>

<style>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  position: relative; /* Para que la X se posicione correctamente */
  background-color: rgb(223, 221, 221);
  padding: 20px;
  border-radius: 8px;
  width: 400px;
  max-width: 90%;
  color: black;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  border: none;
  background: transparent;
  font-size: 20px;
  cursor: pointer;
  color: black;
}
</style>
