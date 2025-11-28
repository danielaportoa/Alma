# 🌿 Proyecto Alma | Sistema de Diseño

> **Documentación de Estilos**
---

## 1. Identidad Visual

### 🎨 Paleta de Colores
Colores definidos para mantener la consistencia de la marca "Alma".

| Categoría | Muestra | Nombre | Hexadecimal | Variable CSS | Uso Principal |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Marca** | 🟤 | **Terracota** | `#C06C55` | `--color-terracota` | Acentos, títulos destacados. |
| **Marca** | 🌿 | **Primary** | `#4F6D56` | `--color-primary` | Botones (CTA), bordes, iconos. |
| **Neutro** | 🦴 | **Hueso** | `#F0E6DC` | `--color-hueso` | Contrastes suaves, textos "small". |
| **Base** | ⚫ | **Dark Earth**| `#2C2B29` | `--color-dark` | Footer, textos de lectura, hovers. |
| **Base** | ⚪ | **Blanco** | `#FFFFFF` | N/A | Fondos generales, tarjetas. |

### ✒️ Tipografía
Fuentes importadas desde Google Fonts.

#### Principal (Serif)
* **Fuente:** `Cormorant Garamond`
* **Pesos:** 400 (Regular), 600 (Semi-bold), 700 (Bold).
* **Aplicación:** Títulos de secciones, Hero Banner, Nombres de productos.

#### Secundaria (Sans-Serif)
* **Fuente:** `Lato`
* **Pesos:** 300 (Light), 400 (Regular), 700 (Bold).
* **Aplicación:** Textos de párrafo, botones, menús de navegación, precios.

---

## 2. Implementación Técnica (CSS)

Copia y pega estos bloques en tu archivo `assets/css/custom.css`.

### 🔧 Variables Globales (`:root`)
Definición de tokens de diseño para facilitar cambios futuros.

```css
:root {
    /* --- Paleta de Colores --- */
    --color-terracota: #C06C55;
    --color-hueso:     #F0E6DC;
    --color-primary:   #4F6D56; /* Verde Bosque desaturado */
    --color-dark:      #2C2B29;
    
    /* --- Tipografías --- */
    --font-titulo:     'Cormorant Garamond', serif;
    --font-cuerpo:     'Lato', sans-serif;
}