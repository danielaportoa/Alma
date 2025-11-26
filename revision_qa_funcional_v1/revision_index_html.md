# 📝 Revisión del Archivo `index.html`

Esta revisión se basa en el **Checklist Ampliado** de buenas prácticas y en las especificaciones funcionales del documento "Estructura.de.la.pagina.pdf".

## 🐞 1. Hallazgos Críticos Funcionales (QA Box Testing)

Estos son fallos directos en la experiencia del usuario que violan la funcionalidad esperada y requieren corrección urgente.

| Elemento                | Problema Funcional Identificado                                                                             | Categoría y Comentario                                                                           |
| :---------------------- | :---------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| **Menú Principal**      | Los enlaces **"Rostro" y "Cuerpo"** llevan al mismo sitio (`href="#"`).                                     | **CRÍTICO:** Falla de navegación. Deben apuntar a sus respectivas secciones o URLs de categoría. |
| **Productos**           | El botón **"Agregar"** en las tarjetas de producto es inactivo y no añade ítems al carrito.                 | **CRÍTICO:** Falla la conversión. La funcionalidad de compra está ausente.                       |
| **Sección Promociones** | Los botones **"Ver Detalles"** de las promociones redirigen incorrectamente al inicio (`href="#"`).         | **ALTO:** Deben llevar a una página de detalles, a un modal de T&C, o a la URL de la promoción.  |
| **Header**              | La **Lupa de búsqueda** no permite buscar ni abre la interfaz de búsqueda.                                  | **ALTO:** Falla la usabilidad. La funcionalidad de búsqueda está ausente.                        |
| **Botón Flotante**      | El botón de **WhatsApp** (al desplegarse) no funciona, ya que el `href` no es un enlace real a `wa.me/...`. | **ALTO:** El enlace debe estar configurado para iniciar un chat con el número de contacto.       |

---

## ⚙️ 2. Hallazgos Técnicos (Revisión de Código)

Estos problemas afectan la **mantenibilidad, la accesibilidad y el rendimiento** del código.

### 2.1. Limpieza de CSS y HTML (Reglas de Separación)

| Checklist               | Problema Identificado                                                                                 | Solución Técnica Requerida                                                                                                                                |
| :---------------------- | :---------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cero Estilos Inline** | **Estilos en Navbar:** La marca "El Alma" usa `style="color: var(--color-marron-oscuro);"`.           | **Corregir:** Mover la definición de color a una clase CSS (ej: `.logo-color`) y aplicarla.                                                               |
| **Cero Estilos Inline** | **Estilos en Footer:** El enlace de "Términos y Condiciones" usa `style="font-size: 0.9rem;"`.        | **Corregir:** Mover la definición del tamaño de fuente a una clase CSS.                                                                                   |
| **Cero Estilos Inline** | **Estilos en Botón Flotante:** La posición (`position: fixed;`, `z-index: 1050;`) se define _inline_. | **Corregir:** Mover estas propiedades cruciales a una clase CSS llamada `.float-button-position`.                                                         |
| **Separación HTML/JS**  | **Función `onclick` Inline:** El botón de ayuda flotante llama a `onclick="toggleFloatMenu()"`.       | **Corregir:** Eliminar el atributo `onclick`. El evento debe ser manejado en `main.js` usando jQuery: `$('#id-del-boton').on('click', toggleFloatMenu);`. |

### 2.2. Estructura y Semántica

| Checklist                | Problema Identificado                                                                                                                                                                                    | Solución Técnica Requerida                                                                                                                                          |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Etiquetas Semánticas** | **Falta la etiqueta `<main>`:** El contenido principal del sitio está disperso en `<div>` y `<section>`s.                                                                                                | **Corregir:** Envolver todo el contenido relevante (Hero, Productos, Envíos, Promociones) entre las etiquetas `<main>` y `</main>`.                                 |
| **Accesibilidad (A11Y)** | **Enlaces del Footer sin `aria-label`:** Los iconos sociales (Facebook, Instagram) son enlaces sin texto visible.                                                                                        | **Corregir:** Agregar un atributo `aria-label` descriptivo a cada enlace (ej: `aria-label="Perfil de Instagram"`).                                                  |
| **Coherencia Bootstrap** | **Breakpoints Desperdiciados:** El código usa `col-12 col-md-4` para las tarjetas. La estrategia _Mobile-First_ indica que `col-12` es redundante si no hay un `col-sm` intermedio, aunque es funcional. | **Sugerencia:** Asegurar que si hay una columna en móvil es `col-12` por defecto, o que se usen `col-sm` si se requieren divisiones intermedias en vistas pequeñas. |
