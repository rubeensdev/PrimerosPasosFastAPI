<template>
  <div id="app">
    <FormularioLogin v-if="mostrarFormulario" @loginExitoso="onLoginExitoso" />
    <!-- Usar :key para forzar re-montaje del componente -->
    <TablaPeliculas v-else-if="mostrarPeliculas" :key="componentKey" />
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>