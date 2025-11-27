- El archivo `main.css` y `styles.css` son 100% idénticos.
- Los archivos `custom.css` y `styles.css` son 99% idénticos, solo se diferencian en el siguiente extracto.

```css
.navbar-brand-img {
  aspect-ratio: 1 / 1; /* Mantiene la imagen cuadrada siempre */
  object-fit: cover; /* Asegura que rellene el cuadrado */
  max-width: 60px; /* Tamaño máximo para la imagen del logo */
}
/*Se aplica css custom para solucionar alineacion de imagen y textos (col-base) en el footer*/
.col-base {
  align-items: flex-end;
}
@media (min-width: 576px) {
  .span-margen-top {
    display: inline-flex;
    height: 69px;
    align-items: flex-end;
  }
}
@media (max-width: 990px) {
  /* --- ESTILOS DE NAVEGACIÓN ANIMADOS --- */
  .nav-link {
    color: var(--color-texto);
    font-weight: 500;
    margin: 0 10px;
    position: relative; /* Necesario para posicionar el ::after */
    transition: color 0.5s ease, transform 0.5s ease;
    padding-bottom: 5px;
  }

  .nav-link:hover {
    color: var(--color-terracota);
  }

  /* La línea animada (inicialmente invisible/sin ancho) */
  .nav-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 5%; /* Empezamos desde el centro */
    transform: translateX(-50%);
    width: 0%; /* Ancho inicial 0 */
    height: 2px;
    background-color: var(--color-terracota);
    transition: width 0.5s cubic-bezier(0.25, 0.8, 0.25, 1); /* Animación suave */
    border-radius: 2px;
  }

  /* Estado Activo (Scroll Spy) */
  .nav-link.active {
    color: var(--color-terracota) !important;
    font-weight: 700;
    transform: translateY(-2px); /* Pequeña elevación del texto */
  }

  /* Expandir la línea cuando está activo */
  .nav-link.active::after {
    width: 10%; /* Se expande al 80% del ancho del texto */
  }

  /* Efecto Hover opcional (para que también se anime al pasar el mouse) */
  .nav-link:hover::after {
    width: 10%;
    opacity: 0.5;
  }
}
```
