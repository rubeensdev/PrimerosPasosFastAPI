<template>
  <div class="container-responsive">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
      <div>
        <h1 class="text-gradient">Tu Biblioteca</h1>
        <p class="text-gray-600 mt-2">
          Total de películas: <span class="text-2xl font-bold text-primary-600">{{ almacen.totalPeliculas }}</span>
        </p>
      </div>
      <div class="flex items-end">
        <button 
          @click="showCrear = true"
          class="btn-primary flex items-center justify-center gap-2 w-full md:w-auto group"
        >
          <span class="text-2xl">➕</span>
          <span>Agregar Película</span>
        </button>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
      <div
        v-for="p in almacen.peliculas"
        :key="p.idPelicula"
        :class="[
          'card group transform transition-all duration-300 hover:scale-105',
          ultimaCreada === p.idPelicula && 'ring-4 ring-green-500 animate-bounce-subtle',
          ultimaActualizada === p.idPelicula && 'ring-4 ring-blue-500 animate-bounce-subtle',
          ultimaEliminada === p.idPelicula && 'ring-4 ring-red-500 animate-bounce-subtle'
        ]"
      >
        <div class="card-header">
          <h3 class="line-clamp-2">{{ p.titulo }}</h3>
        </div>
        <div class="card-body space-y-3">
          <div class="grid grid-cols-2 gap-4">
            <div class="bg-primary-50 rounded-lg p-3 text-center">
              <p class="text-xs text-gray-600 font-semibold">Año</p>
              <p class="text-2xl font-bold text-primary-600">{{ p.ano }}</p>
            </div>
            <div class="bg-secondary-50 rounded-lg p-3 text-center">
              <p class="text-xs text-gray-600 font-semibold">Género</p>
              <p class="text-sm font-bold text-secondary-600">{{ p.genero }}</p>
            </div>
          </div>
          
          <p class="text-sm text-gray-600">
            ID: <span class="font-mono font-semibold">#{{ p.idPelicula }}</span>
          </p>

          <!-- Botones de Acción -->
          <div class="flex gap-2 pt-4 border-t border-gray-100">
            <button
              @click="abrirEditar(p)"
              class="btn-secondary flex-1 py-2 text-sm flex items-center justify-center gap-1 group/btn"
            >
              <span>✏️</span>
              <span class="hidden sm:inline">Editar</span>
            </button>
            <button
              @click="eliminarPelicula(p.idPelicula)"
              class="btn-danger flex-1 py-2 text-sm flex items-center justify-center gap-1 group/btn"
            >
              <span>🗑️</span>
              <span class="hidden sm:inline">Borrar</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Vista Tabla (para escritorio) -->
    <div class="hidden lg:block mb-8">
      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full">
            <thead class="card-header">
              <tr>
                <th class="px-6 py-4 text-left text-lg font-semibold">ID</th>
                <th class="px-6 py-4 text-left text-lg font-semibold">Título</th>
                <th class="px-6 py-4 text-center text-lg font-semibold">Año</th>
                <th class="px-6 py-4 text-center text-lg font-semibold">Género</th>
                <th class="px-6 py-4 text-center text-lg font-semibold">Acciones</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">
              <tr
                v-for="p in almacen.peliculas"
                :key="p.idPelicula"
                :class="[
                  'transition-all duration-300 hover:bg-primary-50',
                  ultimaCreada === p.idPelicula && 'bg-green-200 animate-pulse',
                  ultimaActualizada === p.idPelicula && 'bg-blue-200 animate-pulse',
                  ultimaEliminada === p.idPelicula && 'bg-red-200 animate-pulse'
                ]"
              >
                <td class="px-6 py-4 font-mono text-sm font-semibold text-gray-700">#{{ p.idPelicula }}</td>
                <td class="px-6 py-4 font-semibold text-gray-900">{{ p.titulo }}</td>
                <td class="px-6 py-4 text-center font-bold text-primary-600">{{ p.ano }}</td>
                <td class="px-6 py-4 text-center">
                  <span class="inline-block bg-secondary-100 text-secondary-700 px-3 py-1 rounded-full text-sm font-semibold">
                    {{ p.genero }}
                  </span>
                </td>
                <td class="px-6 py-4 text-center space-x-2">
                  <button
                    @click="abrirEditar(p)"
                    class="btn-secondary inline-flex items-center gap-1 py-2 px-3 text-sm"
                  >
                    ✏️ Editar
                  </button>
                  <button
                    @click="eliminarPelicula(p.idPelicula)"
                    class="btn-danger inline-flex items-center gap-1 py-2 px-3 text-sm"
                  >
                    🗑️ Borrar
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Toggle JSON Depuración -->
    <div class="flex justify-center mb-8">
      <button
        @click="mostrarJSON = !mostrarJSON"
        class="btn-ghost flex items-center gap-2"
      >

        <span>{{ mostrarJSON ? 'Ocultar' : 'Mostrar' }} JSON (Depuración)</span>
      </button>
    </div>

    <!-- JSON Depuración -->
    <div
      v-if="mostrarJSON"
      class="card mb-8 max-h-96 overflow-y-auto animate-fade-in"
    >
      <div class="card-header">
        <h3>📊 JSON de Datos (Depuración)</h3>
      </div>
      <div class="card-body bg-gray-900 rounded-b-lg">
        <pre class="text-xs text-green-400 font-mono overflow-x-auto">{{ JSON.stringify(almacen.peliculas, null, 2) }}</pre>
      </div>
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
table {
  @apply border-collapse w-full;
}

table tbody tr:hover {
  @apply bg-primary-50;
}
</style>