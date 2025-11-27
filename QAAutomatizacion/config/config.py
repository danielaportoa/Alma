"""
Configuración central para el framework de automatización QA con Playwright
Aquí defines todas las variables globales y configuraciones
"""

import os
from pathlib import Path

# ============================================================================
# CONFIGURACIÓN DE LA APLICACIÓN A PROBAR
# ============================================================================

# URL base de la aplicación (cámbiala por la URL de tus compañeros)
BASE_URL = "http://localhost:8000"  # Ejemplo: servidor local

# URL alternativa para testing con archivo local
# Obtiene la ruta absoluta del archivo de prueba
PROJECT_ROOT = Path(__file__).parent.parent
TEST_PAGE_PATH = PROJECT_ROOT / "test_data" / "test_page.html"
TEST_PAGE_URL = f"file:///{TEST_PAGE_PATH.as_posix()}"

# ============================================================================
# CONFIGURACIÓN DE NAVEGADORES
# ============================================================================

# Navegador a usar: 'chromium', 'firefox', 'webkit' (Safari)
BROWSER = 'chromium'

# Modo headless (sin interfaz gráfica, más rápido)
HEADLESS = False  # Cambiar a True para ejecución en CI/CD

# Tamaño de ventana del navegador
WINDOW_SIZE = {
    'width': 1920,
    'height': 1080
}

# Tamaños para pruebas responsive
RESPONSIVE_SIZES = {
    'mobile': {'width': 375, 'height': 667},      # iPhone SE
    'tablet': {'width': 768, 'height': 1024},     # iPad
    'desktop': {'width': 1920, 'height': 1080},   # Desktop
}

# ============================================================================
# CONFIGURACIÓN DE TIMEOUTS
# ============================================================================

# Tiempo máximo de espera para elementos (segundos)
DEFAULT_TIMEOUT = 10000  # Playwright usa milisegundos
PAGE_LOAD_TIMEOUT = 30000

# ============================================================================
# CONFIGURACIÓN DE PLAYWRIGHT
# ============================================================================

PLAYWRIGHT_CONFIG = {
    'slow_mo': 0,            # Ralentizar acciones (ms) - útil para demos
    'video': False,          # Grabar video de las pruebas
    'screenshot': 'only-on-failure',  # 'on', 'off', 'only-on-failure'
    'trace': 'retain-on-failure',     # Trace para debugging
}

# ============================================================================
# CONFIGURACIÓN DE REPORTES
# ============================================================================

# Directorio para screenshots
SCREENSHOTS_DIR = PROJECT_ROOT / "reports" / "screenshots"
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

# Directorio para reportes HTML
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================================
# CONFIGURACIÓN DE LOGS
# ============================================================================

# Nivel de logging: 'DEBUG', 'INFO', 'WARNING', 'ERROR'
LOG_LEVEL = 'INFO'

# Directorio de logs
LOGS_DIR = PROJECT_ROOT / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================================
# DATOS DE PRUEBA
# ============================================================================

# Datos de prueba para formularios
TEST_DATA = {
    'user': {
        'name': 'Test User',
        'email': 'testuser@example.com',
        'password': 'TestPassword123!',
        'phone': '+1234567890'
    },
    'product': {
        'name': 'Test Product',
        'price': '99.99',
        'quantity': '5'
    }
}

# ============================================================================
# FUNCIONES HELPER
# ============================================================================

def get_base_url():
    """Retorna la URL base configurada"""
    return BASE_URL

def get_test_page_url():
    """Retorna la URL de la página de prueba local"""
    return TEST_PAGE_URL

def get_browser_config():
    """
    Retorna configuración del navegador para Playwright
    
    Returns:
        dict: Configuración del navegador
    """
    return {
        'headless': HEADLESS,
        'slow_mo': PLAYWRIGHT_CONFIG['slow_mo'],
        'viewport': WINDOW_SIZE,
    }
