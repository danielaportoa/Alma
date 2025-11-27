"""
Funciones helper para facilitar las pruebas con Playwright
Utilidades comunes reutilizables en todo el framework
"""

import time
import os
from datetime import datetime
from config.config import SCREENSHOTS_DIR


def take_screenshot(page, test_name):
    """
    Captura un screenshot y lo guarda con nombre descriptivo
    
    Args:
        page: Instancia de Playwright Page
        test_name (str): Nombre de la prueba
        
    Returns:
        str: Ruta del screenshot guardado
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOTS_DIR, filename)
    
    page.screenshot(path=filepath)
    
    print(f"📸 Screenshot guardado: {filepath}")
    return filepath


def generate_timestamp():
    """
    Genera un timestamp formateado
    
    Returns:
        str: Timestamp en formato YYYYMMDD_HHMMSS
    """
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def log_test_step(step_description):
    """
    Imprime un paso de prueba formateado
    
    Args:
        step_description (str): Descripción del paso
    """
    print(f"\n{'='*60}")
    print(f"🧪 PASO: {step_description}")
    print(f"{'='*60}\n")


def wait_for_page_load(page, timeout=30):
    """
    Espera a que la página cargue completamente
    
    Args:
        page: Instancia de Playwright Page
        timeout (int): Tiempo máximo de espera en segundos
    """
    page.wait_for_load_state("domcontentloaded", timeout=timeout*1000)
    page.wait_for_load_state("networkidle", timeout=timeout*1000)


def highlight_element(page, selector, duration=1):
    """
    Resalta un elemento visualmente (útil para demos)
    
    Args:
        page: Instancia de Playwright Page
        selector (str): Selector CSS del elemento
        duration (int): Duración del resaltado en segundos
    """
    page.evaluate(f"""
        (selector, duration) => {{
            const element = document.querySelector(selector);
            if (element) {{
                const originalStyle = element.getAttribute('style');
                element.setAttribute('style', 
                    'border: 3px solid red !important; background-color: yellow !important;');
                setTimeout(() => {{
                    element.setAttribute('style', originalStyle || '');
                }}, duration * 1000);
            }}
        }}
    """, selector, duration)
    time.sleep(duration)


def get_element_info(page, selector):
    """
    Obtiene información detallada de un elemento
    
    Args:
        page: Instancia de Playwright Page
        selector (str): Selector CSS del elemento
        
    Returns:
        dict: Información del elemento
    """
    return page.evaluate(f"""
        (selector) => {{
            const element = document.querySelector(selector);
            if (!element) return null;
            
            const rect = element.getBoundingClientRect();
            return {{
                tag: element.tagName.toLowerCase(),
                text: element.textContent,
                visible: element.offsetParent !== null,
                location: {{ x: rect.x, y: rect.y }},
                size: {{ width: rect.width, height: rect.height }},
                attributes: {{
                    id: element.id,
                    className: element.className,
                    name: element.getAttribute('name'),
                }}
            }};
        }}
    """, selector)


def scroll_to_element(page, selector):
    """
    Hace scroll hasta un elemento
    
    Args:
        page: Instancia de Playwright Page
        selector (str): Selector CSS del elemento
    """
    page.locator(selector).scroll_into_view_if_needed()
    time.sleep(0.5)


def get_css_property(page, selector, property_name):
    """
    Obtiene el valor de una propiedad CSS
    
    Args:
        page: Instancia de Playwright Page
        selector (str): Selector CSS del elemento
        property_name (str): Nombre de la propiedad CSS
        
    Returns:
        str: Valor de la propiedad
    """
    return page.locator(selector).evaluate(
        f"el => getComputedStyle(el).{property_name}"
    )


def compare_colors(actual_color, expected_color):
    """
    Compara dos colores (soporta diferentes formatos)
    
    Args:
        actual_color (str): Color actual (rgba, rgb, hex)
        expected_color (str): Color esperado
        
    Returns:
        bool: True si los colores coinciden
    """
    # Normalizar colores a formato rgba
    def normalize_color(color):
        if color.startswith('rgba'):
            return color
        elif color.startswith('rgb'):
            # Convertir rgb a rgba
            rgb_values = color.replace('rgb(', '').replace(')', '')
            return f'rgba({rgb_values}, 1)'
        elif color.startswith('#'):
            # Convertir hex a rgba
            hex_color = color.lstrip('#')
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            return f'rgba({r}, {g}, {b}, 1)'
        return color
    
    return normalize_color(actual_color) == normalize_color(expected_color)


def handle_alert(page, accept=True):
    """
    Maneja un diálogo de alerta
    
    Args:
        page: Instancia de Playwright Page
        accept (bool): True para aceptar, False para cancelar
        
    Returns:
        str: Mensaje de la alerta
    """
    dialog_message = []
    
    def handle_dialog(dialog):
        dialog_message.append(dialog.message)
        if accept:
            dialog.accept()
        else:
            dialog.dismiss()
    
    page.on("dialog", handle_dialog)
    return dialog_message
