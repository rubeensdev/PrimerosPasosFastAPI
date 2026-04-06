from schemas import PeliculaCreate

def test_crear_pelicula_schema():
    # Verificamos que el esquema de Pydantic funciona correctamente
    datos = {"titulo": "Inception", "genero": "Sci-Fi", "ano": 2010}
    pelicula = PeliculaCreate(**datos)
    assert pelicula.titulo == "Inception"
    assert pelicula.ano == 2010