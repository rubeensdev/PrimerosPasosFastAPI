# 🚀 Primeros Pasos FastAPI - Despliegue en Producción

Estructura organizada para desplegar frontend y backend en diferentes plataformas.

## 📋 Estructura del Proyecto

```
PrimerosPasosFastAPI/
├── frontend/          → 🎨 Vue.js (Vercel)
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vercel.json
│
├── backend/           → 🔧 FastAPI (Render)
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── alembic/
│   ├── requirements.txt
│   └── render.yaml
│
└── README.md          (Este archivo)
```

---

## 🌐 Plataformas de Despliegue

### 1. **FRONTEND → Vercel** 🎨
- **Plataforma**: Vercel.com
- **Qué sube**: Carpeta `frontend/`
- **Framework**: Vue.js 3
- **URLs**: 
  - Staging: https://tu-app-staging.vercel.app
  - Production: https://tu-app.vercel.app

### 2. **BACKEND → Render** 🔧
- **Plataforma**: Render.com
- **Qué sube**: Carpeta `backend/`
- **Framework**: FastAPI + Python
- **URL**: https://fastapi-app.onrender.com

---

## ⚙️ Pasos de Despliegue

### Paso 1: Preparar Frontend (Vercel)

```bash
# 1. Conectar repositorio en Vercel.com
# 2. Seleccionar: "Import Git Repository"
# 3. Configurar:
#    - Root Directory: frontend
#    - Framework: Vite (o dejar en Auto)
#    - Build Command: npm run build
#    - Output Directory: dist
```

**Variables de Entorno en Vercel:**
```
VITE_API_URL=https://fastapi-app.onrender.com
```

### Paso 2: Preparar Backend (Render)

```bash
# 1. Conectar repositorio en Render.com
# 2. Crear "New Web Service"
# 3. Configurar:
#    - Root Directory: backend
#    - Environment: Python 3
#    - Build Command: pip install -r requirements.txt
#    - Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Variables de Entorno en Render:**
```
DATABASE_URL=postgresql://usuario:contraseña@host:5432/db
SECRET_KEY=tu-clave-secreta-muy-larga
CORS_ORIGINS=https://tu-app.vercel.app
```

---

## 🔒 Variables de Entorno

### Desarrollo Local

**`frontend/.env.local`:**
```
VITE_API_URL=http://localhost:8000
```

**`backend/.env`:**
```
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=dev-secret-key-123
ENVIRONMENT=development
CORS_ORIGINS=http://localhost:5173
```

### Producción

**Vercel** (Settings → Environment Variables):
```
VITE_API_URL=https://fastapi-app.onrender.com
```

**Render** (Settings → Environment):
```
DATABASE_URL=postgresql://...
SECRET_KEY=prod-secret-key-muy-segura
CORS_ORIGINS=https://tu-app.vercel.app
```

---

## 📊 Resumen de Puertos

| Servicio | Ambiente | Puerto | URL |
|----------|----------|--------|-----|
| Vue.js | Local | 5173 | http://localhost:5173 |
| FastAPI | Local | 8000 | http://localhost:8000 |
| Vue.js | Producción | 443 | https://tu-app.vercel.app |
| FastAPI | Producción | Auto | https://fastapi-app.onrender.com |

---

## 🔄 Flujo de Despliegue

```
Git Push (a rama main)
    ↓
GitHub Webhook → Vercel (detecta cambios en frontend/)
                 Vercel: Build → Deploy
    ↓
GitHub Webhook → Render (detecta cambios en backend/)
                 Render: Build → Deploy
    ↓
Tu aplicación en línea ✅
```

---

## 🛠️ Comandos Útiles

### Frontend
```bash
cd frontend
npm install
npm run serve          # Desarrollo
npm run build          # Build para producción
npm run lint           # Verificar código
```

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload              # Desarrollo
alembic upgrade head                   # Migraciones
```

---

## 🚨 Solución de Problemas

### CORS Error
**Solución**: Asegurate que `CORS_ORIGINS` en Render coincida con tu URL de Vercel

### 404 en Vercel
**Solución**: Revisa que `vercel.json` tenga las reescrituras correctas

### Base de Datos en Render
**Solución**: Usa Render Database o una BD externa (PostgreSQL)

---

## 📚 Documentación Útil

- [Vercel Docs](https://vercel.com/docs)
- [Render Docs](https://render.com/docs)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [Vue.js Docs](https://vuejs.org)

---

**Hecho por:** Tu equipo  
**Última actualización:** 23 de Enero 2026
