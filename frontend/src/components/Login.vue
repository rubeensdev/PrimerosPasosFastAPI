<template>
  <div class="login-container">
    <h2>Inicia sesion para poder ver el listado de peliculas.</h2>
    <form @submit.prevent="login">
      <div class="formulario">
        <label for="usuario">Usuario:</label>
        <input type="text" id="usuario" v-model="usuario" placeholder="Introduce tu usuario" required />
      </div>

      <div class="formulario">
        <label for="password">Contraseña:</label>
        <input type="password" id="password" v-model="password" placeholder="Introduce tu contraseña" required />
      </div>

      <button type="submit">Entrar</button>
    </form>
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


<style>
.login-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  border-radius: 8px;
  background-color: #f5f5f5;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.formulario {
  margin-bottom: 50px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  background-color: #50558f;
  color: white;
  cursor: pointer;
}

button:hover {
  transform: scale(1.2);
  transition: transform 0.3s ease;


}
</style>