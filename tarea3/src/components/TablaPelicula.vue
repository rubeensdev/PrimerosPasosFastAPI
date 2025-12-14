<template>
  <div>
    <h2>Lista de Películas ({{ almacen.totalPeliculas }})</h2>
    <button class="boton" @click="showCrear = true">
      <img src="../imagenes/agregar.png" alt="Agregar" width="50px">
    </button>
    <table align="center" cellpadding="10" cellspacing="0">
      <thead>
        <tr>
          <th>ID</th>
          <th>Título</th>
          <th>Año</th>
          <th>Género</th>
          <th>Acciones</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="p in almacen.peliculas" :key="p.idPelicula" :class="{
          filaCreada: ultimaCreada === p.idPelicula,
          filaActualizada: ultimaActualizada === p.idPelicula,
          filaEliminada: ultimaEliminada === p.idPelicula
        }">
          <td>{{ p.idPelicula }}</td>
          <td>{{ p.titulo }}</td>
          <td>{{ p.ano }}</td>
          <td>{{ p.genero }}</td>
          <td>
            <button class="boton" @click="abrirEditar(p)">
              <img src="../imagenes/editar.png" alt="Editar" width="50px">
            </button>
            <button class="boton" @click="eliminarPelicula(p.idPelicula)">
              <img src="../imagenes/borrar.png" alt="Eliminar" width="50px">
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Depuración -->
    <button @click="mostrarJSON = !mostrarJSON">Mostrar listado y JSON BRUTO  </button>
    <div style="font-size:13px;margin-top:8px;color:#333" v-if="mostrarJSON">
      <pre>{{ JSON.stringify(almacen.peliculas, null, 2) }}</pre>
    </div>

    <!-- MODALES -->
    <EditarPelicula 
      :show="showEditar" 
      :pelicula="almacen.peliculaSeleccionada" 
      @close="showEditar = false"
      @guardar="guardarPeliculaEditada" 
    />

    <CrearPelicula 
      :show="showCrear" 
      @close="showCrear = false" 
      @crear="crearPelicula" 
    />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useAlmacenPeliculas } from '../stores/peliculas'
import EditarPelicula from './EditarPelicula.vue'
import CrearPelicula from './CrearPelicula.vue'

export default {
  name: 'PeliculasTabla',
  components: { EditarPelicula, CrearPelicula },

  setup() {
    const almacen = useAlmacenPeliculas()

    const showEditar = ref(false)
    const showCrear = ref(false)
    const mostrarJSON = ref(false)

    const ultimaCreada = ref(null)
    const ultimaActualizada = ref(null)
    const ultimaEliminada = ref(null)

    // Cargar películas al montar
    onMounted(() => {
      almacen.cargarPeliculas()
    })

    function abrirEditar(p) {
      almacen.seleccionarPelicula(p)
      showEditar.value = true
    }

    // CREAR
    async function crearPelicula(nuevaPeli) {
      await almacen.crearPelicula(nuevaPeli)
      
      // Obtener el ID de la última película creada
      const ultimaPeli = almacen.peliculas[almacen.peliculas.length - 1]
      ultimaCreada.value = ultimaPeli?.idPelicula
      
      setTimeout(() => (ultimaCreada.value = null), 1000)
      showCrear.value = false
    }

    // EDITAR
    async function guardarPeliculaEditada(peliActualizada) {
      ultimaActualizada.value = peliActualizada.idPelicula
      
      await almacen.actualizarPelicula(peliActualizada)
      
      showEditar.value = false
      setTimeout(() => (ultimaActualizada.value = null), 1000)
    }

    // BORRAR
    async function eliminarPelicula(id) {
      ultimaEliminada.value = id

      setTimeout(async () => {
        await almacen.borrarPelicula(id)
        ultimaEliminada.value = null
      }, 1000)
    }

    return {
      almacen,
      mostrarJSON,
      showCrear,
      showEditar,
      ultimaCreada,
      ultimaActualizada,
      ultimaEliminada,
      abrirEditar,
      crearPelicula,
      guardarPeliculaEditada,
      eliminarPelicula
    }
  }
}
</script>

<style scoped>
.filaCreada {
  background-color: #23a24d !important;
  transition: background 0.7s ease;
}

.filaActualizada {
  background-color: #4a88da !important;
  transition: background 0.7s ease;
}

.filaEliminada {
  background-color: #ea2d40 !important;
  transition: background 0.7s ease;
}

.boton {
  background-color: transparent;
  border: none;
  cursor: pointer;
  margin: 0 4px;
}

.boton:hover {
  transform: scale(1.2);
  transition: transform 0.3s ease;
}
</style>