## ✅ Checklist de Revisión de Código Ampliado

Este checklist asegura la calidad, el rendimiento y la mantenibilidad del proyecto **HTML / CSS / Bootstrap / JS / jQuery**.

### 1. Estructura y Bootstrap (La Grilla y la Maquetación)

El foco aquí es asegurar que la estructura base sea correcta y responsiva.

- [ ] **Jerarquía de la Grilla:** ¿Se respeta rigurosamente el orden `container` > `row` > `col-*` en todas las secciones principales?
- [ ] **Estrategia Mobile-First:** ¿Se utilizan clases de columna `col-12` o `col-sm-*` como base para asegurar que el contenido escala correctamente en móviles?
- [ ] **Utilidades de Espaciado:** ¿Se utiliza la sintaxis de Bootstrap (`mt-`, `p-`, `mx-auto`) para definir márgenes y paddings en lugar de escribir CSS personalizado?
- [ ] **Imágenes Responsivas:** ¿Todas las imágenes de contenido (no decorativas de fondo) tienen la clase de Bootstrap `.img-fluid`?
- [ ] **Etiquetas Semánticas:** ¿Se han utilizado las etiquetas HTML5 adecuadas (`<header>`, `<main>`, `<section>`, `<footer>`) en lugar de usar solo `<div>` para la estructura del sitio?

### 2. Limpieza de CSS y HTML (Estilo y Mantenibilidad)

Estos puntos previenen los conflictos y simplifican el mantenimiento del código en el futuro.

- [ ] **Cero Estilos Inline:** ¿Se ha eliminado por completo cualquier atributo `style="..."` que aplique estilos directamente en el HTML?
- [ ] **Prohibición de `!important`:** ¿El archivo CSS está libre de la declaración `!important` (salvo que sea estrictamente necesario para un override de librería y esté comentado)?
- [ ] **Unidades Relativas:** ¿Se usan unidades relativas (`rem`, `em`, `%`) en lugar de `px` para fuentes y espaciados clave para asegurar mejor escalabilidad?
- [ ] **Consistencia de Nombres:** ¿Las clases CSS personalizadas tienen un nombre descriptivo y consistente (ej: `card-product` o `boton-primario`) y no son genéricas o vagas?
- [ ] **Ubicación de CSS:** ¿El archivo CSS personalizado se carga en la etiqueta `<head>` antes que el CSS de Bootstrap (para poder sobrescribir sus estilos si es necesario)?

### 3. Buenas Prácticas Javascript / jQuery (Rendimiento y Lógica)

El objetivo es optimizar el rendimiento y evitar problemas de lógica.

- [ ] **Consola Limpia:** ¿La consola del navegador (F12) está totalmente libre de errores de JavaScript (`Uncaught Type Error`, etc.) y de `console.log()` de depuración?
- [ ] **Separación de Intereses (HTML vs JS):** ¿No hay ninguna llamada a función JS o evento en el HTML (ej: `onclick`, `onchange`, `href="javascript:void(0)"`)?
- [ ] **Cacheo de Selectores:** ¿Se guardan los selectores de jQuery utilizados con frecuencia en variables (ej: `const $btn = $('#id');`) para evitar que jQuery recorra el DOM repetidamente?
- [ ] **Delegación de Eventos:** En el caso de listas grandes o contenido que se carga dinámicamente, ¿se están utilizando eventos delegados (ej: `.on('click', '.clase-hijo', ...)` en un elemento padre)?
- [ ] **Ubicación de Scripts:** ¿Los archivos de scripts `.js` se cargan justo antes de la etiqueta de cierre `</body>` para no bloquear la carga visual de la página?
