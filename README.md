# E-commerce Alma - MVP Frontend

Bienvenido al repositorio del proyecto **E-commerce Alma**, la primera versión (MVP) de una tienda en línea enfocada en la implementación de estructuras semánticas, diseño responsivo y manipulación dinámica del DOM.

## 🚀 Propósito del Proyecto
Desarrollar una interfaz funcional y estética para una tienda virtual, utilizando herramientas modernas de maquetación y scripts básicos de interacción para simular la experiencia de compra de un usuario.

## 📦 Alcance del MVP
El proyecto consta de las siguientes secciones funcionales:
1.  **Inicio (Home):** Exhibición de productos mediante una grilla dinámica con componentes *Card* de Bootstrap.
2.  **Detalle de Producto:** Vista expandida con información técnica, precio y opción de compra.
3.  **Carrito (Simulado):** Sistema de gestión de productos con persistencia sugerida en `localStorage` y contador en tiempo real en la barra de navegación.
4.  **Navegación:** Navbar funcional y Footer con información corporativa ficticia.

---

## 🛠️ Requisitos Técnicos
### Frontend
- **HTML5:** Uso de etiquetas semánticas (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`).
- **Bootstrap 5 (vía CDN):** - Sistema de Grid (Container, Row, Col).
  - Componentes: Navbars, Cards, Buttons, Badges.
  - Utilidades de espaciado (Padding/Margin) y tipografía.
- **JavaScript:** - Selección de elementos (`querySelector`).
  - Manejo de eventos (`addEventListener`).
  - Lógica de renderizado mediante Arrays y Objetos.

### Herramientas de Desarrollo
- **Control de Versiones:** Git con flujo de trabajo en GitHub.
- **Responsive Design:** Optimizado para dispositivos móviles (≤ 420px) y escritorio (≥ 1024px).

---

## 📋 Requisitos Funcionales Mínimos
- [x] Generación dinámica de productos desde un arreglo de objetos en JS.
- [x] Actualización automática del contador del carrito en el Navbar al "Agregar".
- [x] Navegación fluida entre la Home y la página de detalles.
- [x] Diseño adaptativo para múltiples resoluciones.

---

## 📂 Estructura del Repositorio
```text
/
├── index.html          # Página principal
├── product-detail.html # Vista de detalle
├── css/
│   └── styles.css      # Estilos personalizados adicionales
├── js/
│   └── main.js         # Lógica del carrito y renderizado
└── README.md           # Documentación del proyecto
