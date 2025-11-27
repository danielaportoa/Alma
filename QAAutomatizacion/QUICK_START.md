# 🚀 Guía Rápida de Inicio - Playwright QA Automation

## ⚡ Instalación Express (3 minutos)

### 1. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 2. Instalar navegadores para Playwright
```bash
playwright install chromium
```

### 3. ¡Ejecutar tu primera prueba!
```bash
pytest tests/functional_tests/test_functionality.py::TestFunctionalityPlaywright::test_page_title -v -s
```

---

## 🎯 Comandos Más Usados

### Ejecutar TODAS las pruebas
```bash
pytest tests/ -v
```

### Ejecutar solo funcionalidad
```bash
pytest tests/functional_tests/test_functionality.py -v
```

### Ejecutar solo UI/UX
```bash
pytest tests/functional_tests/test_ui_ux.py -v
```

### Generar reporte HTML
```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

### Ejecutar con diferentes navegadores
```bash
# Chromium (default - Chrome)
pytest tests/ --browser chromium -v

# Firefox
pytest tests/ --browser firefox -v

# Safari (WebKit)
pytest tests/ --browser webkit -v
```

---

## 📝 Cómo Adaptar para la Página de tus Compañeros

### Paso 1: Actualizar la URL
Edita `config/config.py` línea 15:
```python
BASE_URL = "http://localhost:3000"  # URL de tu aplicación
```

### Paso 2: Crear pruebas para tu página
Copia cualquier archivo de test y modifica:
```python
def test_mi_funcionalidad(self, page: Page):
    log_test_step("Probando mi funcionalidad")
    
    # Navegar a la página
    page.goto(BASE_URL)
    
    # Interactuar con elementos
    page.click("#mi-boton")
    page.fill("#mi-input", "texto de prueba")
    
    # Verificar resultados
    expect(page.locator("#resultado")).to_have_text("esperado")
    
    print("✅ Test PASSED")
```

### Paso 3: Usar Codegen para generar código automáticamente
```bash
# Playwright abrirá el navegador y grabará tus acciones como código
playwright codegen http://localhost:3000
```

---

## 📊 Interpretando los Resultados

### ✅ Test PASSED
```
test_page_title PASSED
```
La prueba pasó exitosamente.

### ❌ Test FAILED
```
test_page_title FAILED
AssertionError: Título incorrecto
```
La prueba falló. Revisa el mensaje de error.

### 📸 Screenshots
Todos los screenshots se guardan en: `reports/screenshots/`

---

## 🛠️ Herramientas de Playwright

### 1. Codegen - Generador de Código
Graba tus interacciones y genera el código automáticamente:
```bash
playwright codegen test_data/test_page.html
```

### 2. Inspector - Debug Interactivo
Pausa y explora las pruebas paso a paso:
```bash
# Agrega en tu test:
page.pause()
```

### 3. Trace Viewer - Ver Grabaciones
Genera y visualiza traces de las pruebas:
```bash
# En config/config.py
PLAYWRIGHT_CONFIG['trace'] = 'on'

# Luego visualiza:
playwright show-trace trace.zip
```

---

## 🐛 Solución de Problemas

### Error: "playwright not installed"
```bash
playwright install
```

### Error: "No tests collected"
Asegúrate de estar en el directorio correcto:
```bash
cd "c:\Users\ANALISTA DE DATOS\.gemini\antigravity\playground\prismic-pioneer"
```

### Las pruebas van muy rápido
Ralentízalas para demos:
```python
# En config/config.py
PLAYWRIGHT_CONFIG['slow_mo'] = 1000  # 1 segundo por acción
HEADLESS = False  # Ver el navegador
```

### No aparecen los screenshots
Verifica que existe la carpeta:
```bash
mkdir reports\screenshots
```

---

## 💡 Tips para el Bootcamp

### 1. **Demostración Visual**
```python
# En config/config.py
HEADLESS = False  # Mostrar navegador
PLAYWRIGHT_CONFIG['slow_mo'] = 500  # Ralentizar acciones
```

### 2. **Agregar Pausas para Explicar**
```python
import time
time.sleep(2)  # Pausa de 2 segundos
```

### 3. **Resaltar Elementos**
```python
from utils.helpers import highlight_element
highlight_element(page, "#mi-elemento", duration=2)
```

### 4. **Generar Buenos Reportes**
```bash
pytest tests/ --html=reports/mi_reporte.html --self-contained-html
```

---

## 📚 Estructura del Proyecto

```
prismic-pioneer/
├── tests/
│   └── functional_tests/        # Todas las pruebas
│       ├── test_functionality.py
│       └── test_ui_ux.py
├── utils/                       # Utilidades helper
├── config/                      # Configuración
├── test_data/                   # Página HTML de ejemplo
└── reports/                     # Reportes generados
```

---

## 🎓 Conceptos Clave para Explicar en el Bootcamp

### 1. **Playwright Ventajas**
- ⚡ Mucho más rápido que Selenium
- 🎯 Auto-waiting (no necesitas sleeps)
- 🔍 Mejores mensajes de error
- 🎬 Herramientas de debugging increíbles

### 2. **Fixtures de pytest**
- `@pytest.fixture(autouse=True)`: Se ejecuta automáticamente
- Setup: Prepara el ambiente (crea la página)
- Teardown: Limpia automáticamente

### 3. **Locators de Playwright**
```python
page.locator("#id")              # Por ID
page.locator(".class")           # Por clase
page.locator("text=Home")        # Por texto
page.locator("button >> text=Submit")  # Combinado
```

### 4. **Assertions con expect**
```python
expect(page.locator("#title")).to_have_text("Esperado")
expect(page.locator("#button")).to_be_visible()
expect(page.locator("#input")).to_be_enabled()
```

---

## ✨ Playwright vs Selenium

| Característica | Playwright | Selenium |
|---------------|------------|----------|
| **Velocidad** | ⚡⚡⚡ Rápido | 🐢 Lento |
| **Auto-waiting** | ✅ Sí | ❌ No |
| **Debugging** | 🎯 Excelente | 😐 Básico |
| **Codegen** | ✅ Sí | ❌ No |
| **Modernidad** | 🚀 2020+ | 📜 2004 |
| **Facilidad** | 😊 Fácil | 😅 Media |

**Conclusión:** Playwright es la opción moderna y profesional.

---

## 🎬 Demo para el Bootcamp

### Script de Presentación (15 minutos):

1. **Mostrar Codegen** (3 min)
   ```bash
   playwright codegen test_data/test_page.html
   ```
   - Interactuar con la página
   - Mostrar código generado

2. **Mostrar el código del test** (3 min)
   - Explicar estructura
   - Mostrar fixtures de pytest

3. **Ejecutar prueba en vivo** (5 min)
   ```bash
   pytest tests/functional_tests/test_functionality.py::TestFunctionalityPlaywright::test_form_submission -v -s
   ```

4. **Mostrar reporte HTML** (2 min)
   ```bash
   pytest tests/ --html=reports/demo.html --self-contained-html
   ```
   Abrir: `reports/demo.html`

5. **Q&A** (2 min)

---

## 📞 Comandos de Emergencia

Si algo sale mal durante la demo:

```bash
# Reinstalar todo
pip install -r requirements.txt --force-reinstall
playwright install chromium

# Limpiar cache
pytest --cache-clear

# Ejecutar prueba simple y rápida
pytest tests/functional_tests/test_functionality.py::TestFunctionalityPlaywright::test_page_title -v -s
```

---

## 🎯 Próximos Pasos

1. **Familiarízate con codegen**
   ```bash
   playwright codegen
   ```

2. **Lee la documentación**
   https://playwright.dev/python/

3. **Adapta a tu proyecto**
   - Actualiza la URL en config.py
   - Copia tests y modifica
   - Usa codegen para generar código

---

¡Éxito en tu bootcamp con Playwright! 🎉

*Playwright = El futuro del testing web* 🚀
