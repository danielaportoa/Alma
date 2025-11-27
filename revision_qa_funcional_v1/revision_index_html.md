# 📝 Revisión del Archivo `index.html`

El código HTML es de alta calidad en cuanto a maquetación con Bootstrap. Sin embargo, se identifican fallos críticos de usabilidad (funcionalidad ausente) y problemas técnicos de mantenimiento que deben ser resueltos.

## 1. 🐞 Hallazgos Críticos Funcionales (Usabilidad / Falla de Lógica)

Estos fallos impactan directamente en la experiencia del usuario y requieren la implementación de lógica JavaScript para funcionar correctamente, ya que actualmente son placeholders inactivos (`href="#"`).

| Elemento           | Problema Funcional Identificado                                                                                                     | Categoría y Comentario                                                                                                                                       |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Productos**      | Los botones **"Agregar"** tienen datos (`data-id`, `data-price`), pero la funcionalidad para añadirlos al carrito está **ausente**. | **CRÍTICO:** Falla la conversión. La clase `.add-to-cart` no tiene un _listener_ en el JS para actualizar el `offcanvas`.                                    |
| **Navegación**     | Los enlaces **"Rostro" y "Cuerpo"** apuntan al mismo destino (`#productos`).                                                        | **ALTO:** Esto confunde al usuario. Deben ser enlaces a páginas/rutas distintas o, al menos, incluir lógica de filtrado por categoría en el `main.js`.       |
| **Header**         | El botón de **Búsqueda (Lupa)** no ejecuta la lógica para abrir/cerrar el overlay (`#search-overlay`).                              | **ALTO:** La funcionalidad está incompleta. El _overlay_ está oculto con CSS, pero la lógica JS para `open`/`close` y la función de búsqueda están ausentes. |
| **Promociones**    | Los botones **"Ver Detalles"** (y el de "Unirme Ahora") usan `href="#"`.                                                            | **MEDIO:** Estos enlaces son inactivos. Deben apuntar a los términos y condiciones o a la URL de la promoción.                                               |
| **Botón Flotante** | Los enlaces desplegables del FAB (WhatsApp, Teléfono, Email) usan `href="#"`.                                                       | **MEDIO:** Deben ser enlaces funcionales. Especialmente el de WhatsApp (`wa.me/`) y el de Email (`mailto:`).                                                 |

---

## 2. ⚙️ Hallazgos Técnicos (Revisión de Código)

### 2.1. Limpieza de CSS y HTML (Estilo y Mantenibilidad)

| Checklist                  | Problema Identificado                                                                                                       | Solución Técnica Requerida                                                                                                                                                      |
| :------------------------- | :-------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Cero Estilos Inline**    | **Newsletter Button:** El botón del _newsletter_ en el _footer_ usa `style="border-radius: 0 5px 5px 0;"`.                  | **Corregir:** Mover la propiedad `border-radius` a una clase específica (ej: `.btn-newsletter`).                                                                                |
| **Cero Estilos Inline**    | **Promo Card (última):** La última tarjeta de promoción usa `style="border:none;"`.                                         | **Corregir:** Crear una clase CSS (ej: `.promo-no-border`) y aplicarla, manteniendo el estilo fuera del HTML.                                                                   |
| **Prohibido `!important`** | **Uso de Utilitarios:** Las clases utilitarias personalizadas (`.text-terracota`, `.bg-verde`, etc.) utilizan `!important`. | **Acción:** Si bien es común en utilidades, se sugiere revisar si es estrictamente necesario o si se puede optimizar la especificidad del CSS para evitarlo.                    |
| **Prohibido `!important`** | **Estado Activo:** La clase `.nav-link.active` utiliza `!important` para sobrescribir el color.                             | **Acción:** Intentar aumentar la especificidad del selector (`nav ul li a.active`) para evitar el uso de `!important`.                                                          |
| **Separación HTML/JS**     | **PASA**                                                                                                                    | **No se encontraron atributos `onclick` o código JavaScript _inline_**, lo cual es una **excelente práctica**. La lógica JS se ha dejado correctamente para el archivo externo. |

### 2.2. Estructura y Semántica

| Checklist                | Problema Identificado                                                                                               | Solución Técnica Requerida                                                                                                                                     |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Etiquetas Semánticas** | **Falta la etiqueta `<main>`:** El contenido principal del sitio está disperso sin el _wrapper_ semántico adecuado. | **Corregir:** Envolver desde la `<header class="hero-section">` hasta antes del `<footer>` con la etiqueta `<main>`.                                           |
| **Atributos `alt`**      | **PASA**                                                                                                            | Todas las imágenes críticas (`<img>`) tienen un atributo `alt` definido.                                                                                       |
| **Accesibilidad (A11Y)** | **Botón Flotante (FAB):** Los iconos desplegables (WhatsApp, Teléfono, Email) usan solo `title` para accesibilidad. | **Sugerencia:** Es mejor práctica utilizar el atributo `aria-label` para describir el destino del enlace, complementando el `title`.                           |
| **Jerarquía de Grilla**  | **PASA**                                                                                                            | Se respeta la estructura `container` > `row` > `col-*`. El uso de `col-lg-6` o `col-md-4` es un diseño correcto _Mobile First_ que asume `col-12` por defecto. |

### 2.3. Javascript / jQuery

| Checklist                | Problema Identificado  | Solución Técnica Requerida                                                                                                                                            |
| :----------------------- | :--------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ubicación de Scripts** | **PASA**               | Los archivos JS de Bootstrap (`bootstrap.bundle.min.js`) están correctamente ubicados justo antes de la etiqueta de cierre `</body>`.                                 |
| **Cacheo y Delegación**  | **PASA (PREPARACIÓN)** | El HTML está correctamente preparado (con IDs y clases como `add-to-cart`) para que un script externo pueda implementar cacheo y delegación de eventos sin problemas. |
