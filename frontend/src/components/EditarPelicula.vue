<template>
  <div v-if="show" class="modal-overlay">
    <div class="modal-content">
      <!-- X para cerrar manualmente -->
      <button class="close-btn" @click="$emit('close')">X</button>

      <form @submit.prevent="guardar" v-if="localPelicula">
        <h3>
          Editar película: {{ localPelicula.titulo }}
        </h3>

        <label>Título</label>
        <input type="text" v-model="localPelicula.titulo" /><br><br>

        <label>Género</label>
        <input type="text" v-model="localPelicula.genero" /><br><br>

        <label>Año</label>
        <input type="number" v-model="localPelicula.ano" /><br><br>

        <input type="submit" value="Guardar">
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EditarPelicula',
  props: {
    show: Boolean,
    pelicula: Object
  },
  data() {
    return {
      localPelicula: null
    }
  },
  watch: {
    pelicula: {
      handler(newVal) {
        if (newVal) {
          this.localPelicula = { ...newVal }
        }
      },
      immediate: true
    }
  },
  methods: {
    guardar() {
      // Emitimos los datos editados al padre
      this.$emit('guardar', { ...this.localPelicula })
      // Cerramos automáticamente el modal
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
