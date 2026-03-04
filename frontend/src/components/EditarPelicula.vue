<template>
  <transition name="modal-fade">
    <div v-if="show" class="modal-overlay">
      <div class="modal-content transform transition-all duration-300 animate-slide-in" v-if="localPelicula">
        <!-- Header con Close Button -->
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-2xl font-bold text-gradient line-clamp-1">
            ✏️ Editar: {{ localPelicula.titulo }}
          </h2>
          <button
            @click="$emit('close')"
            class="text-3xl text-gray-400 hover:text-gray-600 transition-colors transform hover:scale-110 flex-shrink-0"
          >
            ✕
          </button>
        </div>

        <!-- Información del ID -->
        <div class="bg-primary-50 rounded-lg p-3 mb-6 text-center">
          <p class="text-xs text-gray-600 font-semibold">ID de la Película</p>
          <p class="text-lg font-bold text-primary-600">#{{ localPelicula.idPelicula }}</p>
        </div>

        <!-- Formulario -->
        <form @submit.prevent="guardar" class="space-y-5">
          <!-- Campo Título -->
          <div class="space-y-2">
            <label for="titulo" class="font-semibold text-gray-700">
              🎬 Título
            </label>
            <input
              id="titulo"
              type="text"
              v-model="localPelicula.titulo"
              placeholder="Edita el título"
              required
              class="input-field focus:ring-4 focus:ring-primary-200"
            />
          </div>

          <!-- Campo Género -->
          <div class="space-y-2">
            <label for="genero" class="font-semibold text-gray-700">
              🎭 Género
            </label>
            <input
              id="genero"
              type="text"
              v-model="localPelicula.genero"
              placeholder="Edita el género"
              required
              class="input-field focus:ring-4 focus:ring-primary-200"
            />
          </div>

          <!-- Campo Año -->
          <div class="space-y-2">
            <label for="ano" class="font-semibold text-gray-700">
              📅 Año
            </label>
            <input
              id="ano"
              type="number"
              v-model="localPelicula.ano"
              placeholder="Edita el año"
              min="1900"
              :max="new Date().getFullYear()"
              required
              class="input-field focus:ring-4 focus:ring-primary-200"
            />
          </div>

          <!-- Botones -->
          <div class="flex gap-3 pt-6 border-t border-gray-200">
            <button
              type="button"
              @click="$emit('close')"
              class="btn-ghost flex-1 py-3"
            >
              Cancelar
            </button>
            <button
              type="submit"
              class="btn-primary flex-1 py-3 font-bold"
            >
              Guardar Cambios
            </button>
          </div>
        </form>
      </div>
    </div>
  </transition>
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

<style scoped>
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.3s ease;
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}

.modal-fade-enter-to,
.modal-fade-leave-from {
  opacity: 1;
}
</style>

