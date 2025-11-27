- Archivos `datos.js` y `main.js` no se están usando

He realizado una revisión exhaustiva del archivo `js.js` en relación con la estructura HTML de `index.html` y los principios del _checklist_ de buenas prácticas.

El código JavaScript es funcional en su mayor parte y utiliza buenas prácticas para interactuar con los componentes de Bootstrap, pero presenta fallos críticos de **integración**, **mantenibilidad** y **defensa contra errores funcionales**.

---

## 🛑 1. Fallos de Integración y Funcionalidad Crítica

Estos problemas impiden que el sitio sea dinámico o que la funcionalidad clave sea robusta.

| Elemento                 | Problema Identificado                                | Detalle y Prioridad                                                                                                                                                                                                                                                          |
| :----------------------- | :--------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Integración de Datos** | **El archivo `datos.js` no se importa.**             | **CRÍTICO:** El archivo `js.js` no contiene ninguna sentencia `import { Productos } from './datos.js'`. Esto significa que la aplicación **no utiliza la fuente de datos maestra** y no puede cargar productos dinámicamente, lo cual es la función principal de `datos.js`. |
| **Rendimiento JS**       | **Ubicación incorrecta del script.**                 | **ALTO:** El `index.html` carga `<script src="./assets/js/js.js"></script>` en la etiqueta `<head>`. Esto **bloquea la renderización** de la página hasta que el script se descarga, lo cual es una mala práctica. Debe moverse justo antes del `</body>`.                   |
| **Carrito (Delegación)** | **Uso de `querySelectorAll` en botones de carrito.** | **ALTO (Mantenibilidad):** El script usa `document.querySelectorAll('.add-to-cart')` y luego itera sobre ellos. Si en el futuro los productos se cargan dinámicamente, los nuevos botones **no tendrán el evento** asignado, rompiendo la función de carrito.                |
| **Botón Flotante (FAB)** | **Falta de lógica funcional en los enlaces.**        | **ALTO:** El script solo maneja el _toggle_ visual del FAB (`fabOptions.classList.toggle('open')`). Los enlaces de WhatsApp, Teléfono y Email en el HTML aún usan `href="#"`, y el JS **no corrige** estos enlaces para que sean funcionales (`wa.me/`, `tel:`, `mailto:`).  |
| **Validación de Datos**  | **Ausencia de chequeo de stock.**                    | **ALTO:** El _handler_ del carrito (`addToCart`) no verifica el campo `stock` de los productos. Un producto con `stock: 0` (ej: ID 4 en `datos.js`) podría teóricamente agregarse al carrito si se corrige la integración.                                                   |

---

## 2. 📝 Buenas Prácticas y Calidad de Código

Estos puntos mejoran la mantenibilidad, claridad y robustez del script.

| Checklist                     | Hallazgo                                              | Detalle y Solución Recomendada                                                                                                                                                                                                                        |
| :---------------------------- | :---------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cacheo del DOM**            | **PASA**                                              | Todos los elementos del DOM (Search, FAB, Cart) se seleccionan una sola vez al inicio del `DOMContentLoaded` y se almacenan en variables `const` (ej: `const searchBtn = document.getElementById('search-btn');`), lo cual es una **buena práctica**. |
| **Gestión de Eventos**        | **Múltiples _event listeners_ para el _scroll_.**     | El script no tiene lógica de _scroll_ o _sticky header_ implementada, pero si se agrega, debe usar _throttling_ o _debouncing_ para evitar la sobrecarga del hilo principal. (Actualmente no es un bug, sino una precaución).                         |
| **Inconsistencia de Nombres** | **Uso de nombres genéricos en variables de carrito.** | Las funciones y variables de carrito (`renderCart`, `updateCartCount`, `addToCart`) son claras, pero la variable `let cart` dentro del ámbito local podría ser más descriptiva (ej: `let cartItems`).                                                 |
| **Defensa del Código**        | **Uso de `parseInt()` en la lógica de carrito.**      | El script usa correctamente `parseInt(this.dataset.price)` para asegurar que el precio del HTML se interprete como número, lo cual es una **buena práctica** para evitar errores de tipo en las sumas.                                                |
| **Feedback Visual**           | **PASA**                                              | La implementación de feedback visual en el botón de "Agregar" (cambiar a `btn-success` y un _check_ por 1.5 segundos) es una **excelente práctica de UX**.                                                                                            |
| **Separación de Intereses**   | **PASA**                                              | La lógica de búsqueda y el FAB utilizan manipulación de clases (`classList.add/remove`) en lugar de estilos _inline_, manteniendo la presentación en el CSS.                                                                                          |

---

## 3. 🔎 Fallos de Diseño en la Búsqueda

| Elemento               | Problema Identificado                       | Detalle y Solución Recomendada                                                                                                                                                                                                                                            |
| :--------------------- | :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Diseño de Búsqueda** | **La función de búsqueda está incompleta.** | El _overlay_ de búsqueda y el filtro de productos están implementados. Sin embargo, la sección de resultados (`<div id="no-results">`) se muestra, pero el botón **"Ver todos los productos"** dentro de esa sección no tiene un _event listener_ asignado en el `js.js`. |
| **Búsqueda (Lógica)**  | **Búsqueda simple por `data-title`.**       | La búsqueda solo funciona sobre el atributo `data-title`. Esto es aceptable, pero si la información proviene de `datos.js`, sería más completo buscar en `nombre`, `descripcion` y `categoria`.                                                                           |
