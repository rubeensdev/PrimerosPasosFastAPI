/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
            50:  '#f0f9ff', // Azul muy muy claro (casi blanco)
            100: '#e0f2fe', // Azul cielo muy claro
            200: '#bae6fd', // Azul cielo claro
            300: '#7dd3fc', // Azul cielo medio claro
            400: '#38bdf8', // Azul vibrante claro
            500: '#0ea5e9', // Azul principal (sky blue fuerte)
            600: '#0284c7', // Azul medio intenso
            700: '#0369a1', // Azul oscuro elegante
            800: '#075985', // Azul muy oscuro
            900: '#0c3d66', // Azul profundo (casi navy)
        },
        secondary: {
            50:  '#faf5ff', // Lila muy muy claro (casi blanco)
            100: '#f3e8ff', // Lila muy claro
            200: '#e9d5ff', // Lavanda claro
            300: '#d8b4fe', // Morado claro
            400: '#c084fc', // Violeta medio claro
            500: '#a855f7', // Morado principal vibrante
            600: '#9333ea', // Morado intenso
            700: '#7e22ce', // Morado oscuro
            800: '#6b21a8', // Violeta oscuro elegante
            900: '#581c87', // Morado profundo
        },
      },
      fontFamily: {
        sans: ['Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
      },
      animation: {
        'slide-in': 'slide-in 0.3s ease-out',
        'fade-in': 'fade-in 0.3s ease-out',
        'bounce-subtle': 'bounce-subtle 0.6s ease-in-out',
      },
      keyframes: {
        'slide-in': {
          '0%': { transform: 'translateY(-10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        'fade-in': {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        'bounce-subtle': {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-5px)' },
        },
      },
    },
  },
  plugins: [],
}
