<template>
  <div id="app" class="min-h-screen bg-gradient-to-b from-gray-50 to-white">
    <!-- transicion para un efecrto de suavidad entre los componentes -->
    <transition 
      name="fade" 
      mode="out-in"
    >
      <!-- Login -->
      <FormularioLogin 
        v-if="mostrarFormulario" 
        @loginExitoso="onLoginExitoso"
        key="login"
      />
      <!-- Peliculas -->
      <TablaPeliculas 
        v-else-if="mostrarPeliculas" 
        :key="`movies-${componentKey}`"
      />
    </transition>
  </div>
</template>

<script>
import { ref } from 'vue'
import FormularioLogin from './components/Login.vue'
import TablaPeliculas from './components/TablaPelicula.vue'

export default {
  name: 'App',
  components: { FormularioLogin, TablaPeliculas },
  setup() {
    const mostrarFormulario = ref(true)
    const mostrarPeliculas = ref(false)
    const componentKey = ref(0)

    const onLoginExitoso = () => {
      console.log('Login exitoso, mostrando películas...')
      mostrarFormulario.value = false
      mostrarPeliculas.value = true
      componentKey.value++ // Forzar re-montaje
    }

    return { mostrarFormulario, mostrarPeliculas, onLoginExitoso, componentKey }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Transiciones de Página */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.fade-enter-to,
.fade-leave-from {
  opacity: 1;
}
</style>