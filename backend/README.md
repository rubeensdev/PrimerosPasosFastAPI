# Backend - FastAPI

Este es el backend de la aplicación, desplegado en **Render**.

## 📦 Requisitos
- Python 3.9+
- pip

## 🚀 Desarrollo Local
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## 🔧 Variables de Entorno
Crear archivo `.env`:
```
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=tu-clave-secreta-local
ENVIRONMENT=development
CORS_ORIGINS=http://localhost:5173
```

## 📤 Despliegue en Render
1. Conectar repositorio GitHub
2. Crear nuevo servicio Web
3. Root Directory: `backend`
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Environment Variables (en Render):
   - `DATABASE_URL` = Tu base de datos
   - `SECRET_KEY` = Clave secreta segura
   - `CORS_ORIGINS` = URL del frontend Vercel

## 📁 Estructura
```
backend/
├── main.py           # Aplicación FastAPI
├── models.py         # Modelos SQLAlchemy
├── schemas.py        # Schemas Pydantic
├── database.py       # Conexión BD
├── alembic/          # Migraciones
├── requirements.txt  # Dependencias
├── render.yaml       # Configuración Render
└── .env.production   # Variables producción
```

## 🔒 Migración de Base de Datos
```bash
alembic upgrade head
```
