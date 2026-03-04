<template>
  <div class="min-h-screen flex-center bg-gradient-to-br from-primary-50 via-white to-secondary-50">
    <!-- Card Principal -->
    <div class="card w-full max-w-md mx-4 transform animate-fade-in">
      <div class="card-header text-center">
        <h1 class="text-3xl font-bold text-primary-100"> CineDB</h1>
        <p class="text-primary-100 mt-2">Acceso a tu biblioteca de películas</p>
      </div>

      <!-- Body del Formulario -->
      <div class="card-body">
        <form @submit.prevent="login" class="space-y-6">
          <!-- Campo Usuario -->
          <div class="space-y-2">
            <label for="usuario" class="flex items-center gap-2">
              <span>Usuario</span>
            </label>
            <input
              type="text"
              id="usuario"
              v-model="usuario"
              placeholder="Escribe tu usuario"
              required
              class="input-field focus:ring-4 focus:ring-primary-200"
            />
          </div>

          <!-- Campo Contraseña -->
          <div class="space-y-2">
            <label for="password" class="flex items-center gap-2">
              <span>Contraseña</span>
            </label>
            <input
              type="password"
              id="password"
              v-model="password"
              placeholder="Escribe tu contraseña"
              required
              class="input-field focus:ring-4 focus:ring-secondary-700"
            />
          </div>

          <!-- Botón Entrar -->
          <button
            type="submit"
            class="btn-primary w-full font-bold text-lg py-4 flex items-center justify-center gap-2 group"
          >
            <span>Entrar</span>
          </button>

          <!-- Información -->
          <p class="text-center text-sm text-gray-600 pt-4 border-t border-gray-200">
            Usuario demo: <span class="font-semibold text-primary-600">admin</span>
          </p>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'FormularioLogin',
  emits: ['loginExitoso'], // Declaramos el evento que emitiremos al padre
  setup(props, { emit }) {
    const usuario = ref('')
    const password = ref('')

    const login = async () => {
      try {
        const res = await fetch('http://127.0.0.1:8000/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ nombre: usuario.value, password: password.value })
        })

        console.log('Status:', res.status) // depuración
        console.log('res.ok:', res.ok)

        const data = await res.json()
        console.log('Data recibida:', data) // depuración

        // Emitimos solo si mensaje es correcto
        if (res.ok) {
          emit('loginExitoso')
        } else {
          alert(data.detail || 'Usuario o contraseña incorrectos')
        }

      } catch (err) {
        console.error('Error al loguearse:', err)
      }
    }



    return {
      usuario,
      password,
      login
    }
  }
}
</script>


<style scoped>
/* Las clases principales están en tailwind.css */
</style>