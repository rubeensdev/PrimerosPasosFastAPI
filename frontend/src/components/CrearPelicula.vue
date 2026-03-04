<template>
  <transition name="modal-fade">
    <div v-if="show" class="modal-overlay">
      <div class="modal-content transform transition-all duration-300 animate-slide-in">
        <!-- Header con Close Button -->
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-2xl font-bold text-gradient">Crear Nueva Película</h2>
          <button
            @click="$emit('close')"
            class="text-3xl text-gray-400 hover:text-gray-600 transition-colors transform hover:scale-110"
          >
            ✕
          </button>
        </div>

        <!-- Formulario -->
        <form @submit.prevent="crear" class="space-y-5">
          <!-- Campo Título -->
          <div class="space-y-2">
            <label for="titulo" class="font-semibold text-gray-700">
              Título
            </label>
            <input
              id="titulo"
              type="text"
              v-model="nuevaPelicula.titulo"
              placeholder="Ej: Inception"
              required
              class="input-field focus:ring-4 focus:ring-primary-200"
            />
          </div>

          <!-- Campo Género -->
          <div class="space-y-2">
            <label for="genero" class="font-semibold text-gray-700">
              Género
            </label>
            <input
              id="genero"
              type="text"
              v-model="nuevaPelicula.genero"
              placeholder="Ej: Ciencia Ficción"
              required
              class="input-field focus:ring-4 focus:ring-primary-200"
            />
          </div>

          <!-- Campo Año -->
          <div class="space-y-2">
            <label for="ano" class="font-semibold text-gray-700">
              Año
            </label>
            <input
              id="ano"
              type="number"
              v-model="nuevaPelicula.ano"
              placeholder="Ej: 2010"
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
              Crear Película
            </button>
          </div>
        </form>
      </div>
    </div>
  </transition>
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
