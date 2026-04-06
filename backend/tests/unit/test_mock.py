import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Mock de la función que devuelve películas
def test_listar_peliculas_mock():
    peliculas_falsas = [
        {"idPelicula": 99, "titulo": "Pelicula Mock", "genero": "Terror", "anio": 2024}
    ]
    with patch("main.get_prueba_peliculas", return_value=peliculas_falsas):
        response = client.get("/peliculas")
        assert response.status_code == 200
        assert response.json()[0]["titulo"] == "Pelicula Mock"

# Mock del login simula que el servicio de autenticación responde
def test_login_con_mock(mocker):
    mock_login = mocker.patch("main.login", return_value={"mensaje": "Correcto"})
    response = client.post("/login", json={"nombre": "admin", "password": "admin123"})
    assert response.status_code == 200

# Stub de una dependencia externa como una base de datos para simular su comportamiento sin necesidad de una conexión real
def test_stub_base_datos():
    db_mock = MagicMock()
    db_mock.query.return_value.all.return_value = [
        MagicMock(idPelicula=1, titulo="Pelicula Stub", genero="Acción", anio=2023)
    ]
    resultado = db_mock.query(None).all()
    assert len(resultado) == 1
    assert resultado[0].titulo == "Pelicula Stub"