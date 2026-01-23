# Frontend - Vue.js

Este es el frontend de la aplicación, desplegado en **Vercel**.

## 📦 Requisitos
- Node.js 18+
- npm o yarn

## 🚀 Desarrollo Local
```bash
npm install
npm run serve
```

## 🔧 Variables de Entorno
Crear archivo `.env.local`:
```
VITE_API_URL=http://localhost:8000
```

## 📤 Despliegue en Vercel
1. Conectar repositorio GitHub
2. Root Directory: `frontend`
3. Build Command: `npm run build`
4. Output Directory: `dist`
5. Environment Variable: `VITE_API_URL` = URL del backend en Render

## 📁 Estructura
```
frontend/
├── src/
│   ├── components/     # Componentes Vue
│   ├── stores/        # Estado (Vuex/Pinia)
│   ├── assets/        # Recursos estáticos
│   └── App.vue        # Componente raíz
├── public/            # Archivos públicos
├── package.json       # Dependencias
└── vercel.json        # Configuración Vercel
```
