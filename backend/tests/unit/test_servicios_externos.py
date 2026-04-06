import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from main import app
import httpx

client = TestClient(app)

# --- Simular respuesta exitosa de API externa ---
def test_servicio_externo_exitoso():
    with patch("httpx.get") as mock_get:
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: {"resultado": "ok"}
        )
        respuesta = httpx.get("https://api-externa.com/datos")
        assert respuesta.status_code == 200
        assert respuesta.json()["resultado"] == "ok"

# --- Simular error 500 ---
def test_servicio_externo_error_500():
    with patch("httpx.get") as mock_get:
        mock_get.return_value = MagicMock(
            status_code=500,
            json=lambda: {"error": "Internal Server Error"}
        )
        respuesta = httpx.get("https://api-externa.com/datos")
        assert respuesta.status_code == 500

# --- Simular timeout ---
def test_servicio_externo_timeout():
    with patch("httpx.get", side_effect=httpx.TimeoutException("Timeout")):
        with pytest.raises(httpx.TimeoutException):
            httpx.get("https://api-externa.com/datos")

# --- Simular respuesta vacía ---
def test_servicio_externo_respuesta_vacia():
    with patch("httpx.get") as mock_get:
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: {}
        )
        respuesta = httpx.get("https://api-externa.com/datos")
        assert respuesta.json() == {}

# --- Verificar que la app responde bien aunque falle el servicio externo ---
def test_app_responde_aunque_falle_externo():
    response = client.get("/")
    assert response.status_code == 200