import { defineStore } from "pinia";

export const useAlmacenPeliculas = defineStore("peliculas", {
  state: () => ({
    peliculas: [],
    peliculaSeleccionada: null,
  }),

  getters: {
    totalPeliculas: (state) => state.peliculas.length,
  },

  actions: {
    async cargarPeliculas() {
      try {
        const res = await fetch("https://primerospasosfastapi-1.onrender.com/peliculas");
        const data = await res.json();
        this.peliculas = Array.isArray(data) ? data : [];
      } catch (err) {
        console.error("Error cargando películas:", err);
      }
    },

    async crearPelicula(nuevaPeli) {
      try {
        const res = await fetch("https://primerospasosfastapi-1.onrender.com/crearPelicula", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(nuevaPeli),
        });
        const data = await res.json();
        if (data?.idPelicula) this.peliculas.push(data); // reactivo
      } catch (err) {
        console.error("Error creando película:", err);
      }
    },

    async actualizarPelicula(peliActualizada) {
      try {
        const res = await fetch(
          `https://primerospasosfastapi-1.onrender.com/actualizaPelicula/${peliActualizada.idPelicula}`,
          {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(peliActualizada),
          }
        );
        const data = await res.json();
        const index = this.peliculas.findIndex((p) => p.idPelicula === data.idPelicula);
        if (index !== -1) this.peliculas.splice(index, 1, data); // reactivo
      } catch (err) {
        console.error("Error actualizando película:", err);
      }
    },

    async borrarPelicula(id) {
      try {
        const res = await fetch(`https://primerospasosfastapi-1.onrender.com/borrarPelicula/${id}`, {
          method: "DELETE",
        });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const index = this.peliculas.findIndex((p) => p.idPelicula === id);
        if (index !== -1) this.peliculas.splice(index, 1); // reactivo
      } catch (err) {
        console.error("Error borrando película:", err);
      }
    },

    seleccionarPelicula(peli) {
      this.peliculaSeleccionada = peli;
    },
  },
});