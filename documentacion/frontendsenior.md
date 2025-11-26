# 🌿 Alma - Cosmética Natural

Bienvenido al repositorio frontend de **Alma**. Este proyecto es una implementación de comercio electrónico SPA (Single Page Application) simulada, construida sobre tecnologías web estándar para garantizar el máximo rendimiento, accesibilidad y compatibilidad.

El objetivo es ofrecer una experiencia de compra fluida para productos de cuidado de la piel, priorizando la semántica y la organización del código nativo.

---


![](assets/img/1.jpg)

## 🚀 Características Principales

### 1\. Navegación y UI (Interfaz de Usuario)

* **Barra de Navegación Responsiva:** Implementada con componentes nativos de Bootstrap 5 y personalizada para la identidad de marca de "Alma".
  * Menú colapsable en móviles (Hamburger menu).
  * Enlaces activos: *Inicio, Productos, Contacto*.
* **Diseño Adaptativo:** Grid system de Bootstrap utilizado para asegurar visualización perfecta en Desktop, Tablet y Móvil.

### 2\. Catálogo de Productos (Dinámico)

* Renderizado de productos manipulando el DOM con JavaScript puro.
* Inyección dinámica de tarjetas de productos (imágenes, títulos, precios) desde un array de objetos (JSON simulado).
* Uso de etiquetas HTML5 semánticas (`<article>`, `<figure>`, `<figcaption>`) dentro de las tarjetas.

### 3\. Carrito de Compras (Lógica de Negocio)

* **Persistencia:** Uso de `localStorage` para guardar la selección del usuario si cierra el navegador.
* **Cálculo en Tiempo Real:** Algoritmos en JS Vanilla para sumar totales y actualizar el contador del icono del carrito instantáneamente.
* **Gestión de Stock:** Validaciones básicas para evitar añadir más productos de los disponibles (simulado).

---

## 🛠 Stack Tecnológico

Este proyecto evita la sobrecarga de dependencias innecesarias, volviendo a las bases sólidas del desarrollo web:

* **HTML5 Semántico:** Estructura clara y accesible (`<header>`, `<main>`, `<nav>`, `<footer>`).
* **CSS Framework:** [Bootstrap 5.3](https://getbootstrap.com/) (vía CDN o local) para la maquetación ágil.
* **CSS Custom:** Archivo `styles.css` dedicado para anular variables de Bootstrap y aplicar la identidad visual de "Alma" (colores tierra, tipografías, sombras suaves).
* **JavaScript (ES6+):** Lógica modular sin librerías externas (No jQuery). Uso de *Arrow Functions*, *Template Literals*, y *Event Delegation*.

---

## 📂 Estructura del Proyecto

Para mantener el orden sin un bundler (como Webpack), se utiliza una separación de responsabilidades clara:

```text
 alma-shop/
 ├── index.html          # Página de Inicio (Landing)
 ├── productos.html      # Catálogo completo
 ├── contacto.html       # Formulario y ubicación
 │
 ├── assets/
 │   ├── css/
 │   │   └── styles.css  # Estilos personalizados (override Bootstrap)
 │   ├── js/
 │   │   ├── app.js      # Lógica principal y eventos globales
 │   │   ├── cart.js     # Lógica específica del carrito de compras
 │   │   └── data.js     # Base de datos simulada (Array de productos)
 │   └── img/            # Imágenes de cremas y logo
 │
 └── README.md           # Documentación del proyecto
```

---

## ⚡ Instalación y Uso

Al ser un proyecto estático, no requiere instalación de dependencias de Node.js.

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/danielaportoa/Alma.git
   ```
2. **Ejecutar:**

   * Simplemente abre el archivo `index.html` en tu navegador preferido.
   * **Recomendado:** Utiliza la extensión "Live Server" de VS Code para simular un entorno de servidor local y evitar problemas de CORS si decides cargar JSON externos en el futuro.

---

## 🔍 Detalles de Implementación (Snippet)

Ejemplo de cómo se renderizan los productos usando JS Vanilla y Template Strings, manteniendo el código limpio:

```javascript
// assets/js/app.js
const renderProducts = (products) => {
    const container = document.querySelector('#product-grid');
  
    container.innerHTML = products.map(product => `
        <div class="col-md-4 col-sm-6 mb-4">
            <article class="card h-100 shadow-sm product-card">
                <img src="${product.image}" class="card-img-top" alt="${product.name}">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">${product.name}</h5>
                    <p class="card-text text-muted flex-grow-1">${product.description}</p>
                    <div class="d-flex justify-content-between align-items-center mt-3">
                        <span class="fw-bold fs-5">$${product.price}</span>
                        <button class="btn btn-outline-success btn-add" data-id="${product.id}">
                            Agregar
                        </button>
                    </div>
                </div>
            </article>
        </div>
    `).join('');
};
```

---

## 📝 Roadmap

* [ ] Integración de Fetch API para consumir datos desde un JSON local en lugar de `data.js`.
* [ ] Validación de formulario de contacto usando API de Validación de HTML5 + JS.
* [ ] Modo oscuro (Dark Mode) utilizando variables CSS.

---

**Desarrollado para Alma - Cosmética Natural**
