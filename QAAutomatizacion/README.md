# 🚀 Framework de Automatización QA con Playwright

Framework de automatización QA en Python usando **Playwright** para pruebas de funcionalidad y UI/UX en aplicaciones web.

## 📋 Descripción

Este proyecto contiene un framework completo de automatización de pruebas para páginas web HTML/CSS/JavaScript usando **Playwright**, la herramienta moderna de Microsoft para testing web. Playwright es rápido, confiable y fácil de usar.

## 🎯 ¿Por qué Playwright?

- ⚡ **Rápido**: Mucho más veloz que otras herramientas
- 🎯 **Confiable**: Auto-waiting inteligente, sin pruebas flaky
- 🛠️ **Moderno**: Soporta todas las características web modernas
- 📱 **Multi-browser**: Chrome, Firefox, Safari (WebKit)
- 🎬 **Grabación**: Genera código automáticamente con codegen
- 🔍 **Debugging**: Inspector visual y traces detallados

## 🛠️ Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 📦 Instalación

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Instalar navegadores para Playwright

```bash
playwright install
```

## 📁 Estructura del Proyecto

```
prismic-pioneer/
│
├── tests/
│   └── functional_tests/          # Todas las pruebas
│       ├── test_functionality.py  # Pruebas de funcionalidad
│       └── test_ui_ux.py         # Pruebas de UI/UX
│
├── pages/                         # Page Object Model (POM)
│   ├── base_page.py              # Clase base (opcional para Playwright)
│   └── example_page.py
│
├── utils/                         # Utilidades
│   └── helpers.py                # Funciones helper
│
├── config/                        # Configuración
│   └── config.py
│
├── reports/                       # Reportes generados
│   └── screenshots/
│
├── test_data/                     # Datos de prueba
│   └── test_page.html            # Página de ejemplo
│
├── requirements.txt               # Dependencias
└── README.md                      # Este archivo
```

## 🚀 Cómo Ejecutar las Pruebas

### Ejecutar todas las pruebas
```bash
pytest tests/ -v
```

### Ejecutar pruebas específicas
```bash
# Solo funcionalidad
pytest tests/functional_tests/test_functionality.py -v

# Solo UI/UX
pytest tests/functional_tests/test_ui_ux.py -v

# Una prueba específica
pytest tests/functional_tests/test_functionality.py::TestFunctionalityPlaywright::test_page_title -v -s
```

### Generar reportes HTML
```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

### Ejecutar en modo headless (sin ventana)
```python
# Editar config/config.py
HEADLESS = True
```

### Ejecutar con diferentes navegadores
```bash
# Chromium (default)
pytest tests/ --browser chromium

# Firefox
pytest tests/ --browser firefox

# WebKit (Safari)
pytest tests/ --browser webkit

# Todos los navegadores
pytest tests/ --browser chromium --browser firefox --browser webkit
```

## 📊 Pruebas Incluidas

### ✅ Pruebas de Funcionalidad (10 pruebas)
- Verificación de título de página
- Envío de formularios
- Navegación por links
- Manejo de alertas JavaScript
- Cambios dinámicos de elementos
- Validación de formularios
- Interactividad de campos
- Botones clickeables

### 🎨 Pruebas de UI/UX (12 pruebas)
- Verificación de elementos visibles
- Validación de colores y estilos CSS
- Responsive design (móvil, tablet, desktop)
- Efectos hover
- Legibilidad de texto
- Estilos de navegación
- Animaciones y transiciones

## 🎓 Para el Bootcamp

### Comandos de Demonstración

```bash
# 1. Ver página de prueba
# Abrir test_data/test_page.html en el navegador

# 2. Ejecutar prueba simple
pytest tests/functional_tests/test_functionality.py::TestFunctionalityPlaywright::test_page_title -v -s

# 3. Ejecutar prueba de formulario (visual)
pytest tests/functional_tests/test_functionality.py::TestFunctionalityPlaywright::test_form_submission -v -s

# 4. Generar reporte completo
pytest tests/ --html=reports/demo.html --self-contained-html
```

### Herramientas de Playwright

#### Codegen - Generador de Código
```bash
# Abre el navegador y graba tus acciones como código
playwright codegen test_data/test_page.html
```

#### Inspector
```bash
# Debug interactivo de pruebas
pytest tests/functional_tests/test_functionality.py --headed --slowmo 1000
```

#### Trace Viewer
```bash
# Ver grabación detallada de la prueba
playwright show-trace trace.zip
```

## 📝 Cómo Adaptar a tu Página Web

### 1. Actualizar la URL
Edita `config/config.py`:
```python
BASE_URL = "http://localhost:3000"  # URL de tu aplicación
```

### 2. Escribir nuevas pruebas
```python
def test_mi_funcionalidad(self, page: Page):
    log_test_step("Probando mi funcionalidad")
    
    # Navegar
    page.goto(BASE_URL)
    
    # Interactuar
    page.click("#mi-boton")
    page.fill("#mi-input", "texto")
    
    # Verificar
    expect(page.locator("#resultado")).to_have_text("esperado")
    
    print("✅ Test PASSED")
```

### 3. Usar Page Objects (opcional)
Para proyectos más grandes, usa el patrón POM:
```python
class MiPagina(BasePage):
    def __init__(self, page):
        self.page = page
        
    def hacer_login(self, usuario, password):
        self.page.fill("#username", usuario)
        self.page.fill("#password", password)
        self.page.click("#login-btn")
```

## 🎨 Página HTML de Prueba

El proyecto incluye `test_data/test_page.html` con:
- 📝 Formulario de contacto
- 🔔 Alertas JavaScript
- 🎨 Elementos con cambios dinámicos
- 📱 Diseño responsive
- ✨ Efectos CSS y animaciones

## 💡 Tips y Trucos

### Ver las pruebas ejecutándose
```python
# En config/config.py
HEADLESS = False
PLAYWRIGHT_CONFIG['slow_mo'] = 500  # Ralentizar 500ms cada acción
```

### Capturar screenshots
```python
from utils.helpers import take_screenshot
take_screenshot(page, "mi_test")
```

### Highlighting elementos (para demos)
```python
from utils.helpers import highlight_element
highlight_element(page, "#mi-elemento", duration=2)
```

### Ver información de elementos
```python
from utils.helpers import get_element_info
info = get_element_info(page, "#mi-elemento")
print(info)
```

## 🐛 Troubleshooting

### Error: "playwright not installed"
```bash
playwright install
```

### Error: "No tests collected"
```bash
# Verificar que estás en el directorio correcto
cd "c:\Users\ANALISTA DE DATOS\.gemini\antigravity\playground\prismic-pioneer"
pytest tests/ -v
```

### Las pruebas van muy rápido
```python
# En config/config.py
PLAYWRIGHT_CONFIG['slow_mo'] = 1000  # 1 segundo por acción
```

## 📖 Recursos Adicionales

- [Documentación Playwright](https://playwright.dev/python/)
- [pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://playwright.dev/python/docs/pom)

## 🎯 Ventajas de este Framework

1. **Moderno**: Usa la tecnología más reciente (Playwright)
2. **Rápido**: Las pruebas son mucho más rápidas y confiables
3. **Fácil**: Sintaxis simple y clara
4. **Completo**: Incluye ejemplos de funcionalidad y UI/UX
5. **Profesional**: Usa mejores prácticas de la industria
6. **Documentado**: Código comentado en español

---

**¡Buena suerte en tu bootcamp! 🎓**

*Framework creado específicamente para demostrar capacidades de QA Automation con las herramientas más modernas.*
