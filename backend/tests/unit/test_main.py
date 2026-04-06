from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_raiz_api():
    response = client.get("/")
    assert response.status_code == 200
    assert "API de Películas" in response.json()["mensaje"]

def test_listar_peliculas():
    response = client.get("/peliculas")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_login_exitoso():
    
    payload = {"nombre": "admin", "password": "admin123"}
    response = client.post("/login", json=payload)
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Correcto"}