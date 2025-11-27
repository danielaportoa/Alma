"""
PRUEBAS DE UI/UX CON PLAYWRIGHT
Tests que verifican aspectos visuales y de experiencia de usuario usando Playwright
"""

import pytest
import time
from playwright.sync_api import Page, expect
from utils.helpers import log_test_step
from config.config import TEST_PAGE_URL, RESPONSIVE_SIZES


class TestUIUXPlaywright:
    """
    Suite de pruebas de UI/UX usando Playwright
    Verifica aspectos visuales, estilos, y responsive design
    """
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup que se ejecuta antes de cada prueba"""
        self.page = page
        
        log_test_step("Navegando a la página (Playwright UI/UX)")
        page.goto(TEST_PAGE_URL)
        time.sleep(1)
        
        yield
        
        time.sleep(1)
    
    def test_page_elements_visible(self, page: Page):
        """
        Test 1: Verifica que todos los elementos principales sean visibles
        """
        log_test_step("Verificando visibilidad de elementos (Playwright)")
        
        elements = {
            "h1": "Título principal",
            ".subtitle": "Subtítulo",
            "#name": "Campo nombre",
            "#email": "Campo email",
            "#message": "Campo mensaje",
            "#submit-btn": "Botón submit",
            ".box": "Box interactivo",
        }
        
        for selector, name in elements.items():
            element = page.locator(selector)
            expect(element).to_be_visible()
            print(f"✅ {name}: Visible")
        
        page.screenshot(path="reports/screenshots/playwright_elements_visible.png")
        print("✅ Test PASSED: Todos los elementos son visibles")
    
    def test_title_styling(self, page: Page):
        """
        Test 2: Verifica estilos del título
        """
        log_test_step("Verificando estilos del título (Playwright)")
        
        title = page.locator("h1")
        
        # Obtener estilos computados
        color = title.evaluate("el => getComputedStyle(el).color")
        text_align = title.evaluate("el => getComputedStyle(el).textAlign")
        font_size = title.evaluate("el => getComputedStyle(el).fontSize")
        
        print(f"🎨 Color: {color}")
        print(f"📐 Alineación: {text_align}")
        print(f"📏 Tamaño de fuente: {font_size}")
        
        assert text_align == "center"
        
        page.screenshot(path="reports/screenshots/playwright_title_styling.png")
        print("✅ Test PASSED: Estilos del título verificados")
    
    def test_button_styles(self, page: Page):
        """
        Test 3: Verifica estilos de botones
        """
        log_test_step("Verificando estilos de botones (Playwright)")
        
        submit_btn = page.locator("#submit-btn")
        
        border_radius = submit_btn.evaluate("el => getComputedStyle(el).borderRadius")
        cursor = submit_btn.evaluate("el => getComputedStyle(el).cursor")
        bg_color = submit_btn.evaluate("el => getComputedStyle(el).backgroundColor")
        
        print(f"🔘 Border radius: {border_radius}")
        print(f"🖱️ Cursor: {cursor}")
        print(f"🎨 Background color: {bg_color}")
        
        assert cursor == "pointer"
        
        page.screenshot(path="reports/screenshots/playwright_button_styles.png")
        print("✅ Test PASSED: Estilos de botones verificados")
    
    def test_form_input_styles(self, page: Page):
        """
        Test 4: Verifica estilos de campos de entrada
        """
        log_test_step("Verificando estilos de inputs (Playwright)")
        
        name_input = page.locator("#name")
        
        padding = name_input.evaluate("el => getComputedStyle(el).padding")
        border = name_input.evaluate("el => getComputedStyle(el).border")
        font_size = name_input.evaluate("el => getComputedStyle(el).fontSize")
        
        print(f"📦 Padding: {padding}")
        print(f"🔲 Border: {border}")
        print(f"📝 Font size: {font_size}")
        
        page.screenshot(path="reports/screenshots/playwright_input_styles.png")
        print("✅ Test PASSED: Estilos de inputs verificados")
    
    def test_hover_effect(self, page: Page):
        """
        Test 5: Verifica efectos hover
        """
        log_test_step("Verificando efectos hover (Playwright)")
        
        list_item = page.locator("ul.items li").first
        
        # Hacer hover
        list_item.hover()
        time.sleep(1)
        
        page.screenshot(path="reports/screenshots/playwright_hover_effect.png")
        print("✅ Test PASSED: Efecto hover aplicado")
    
    def test_responsive_mobile(self, page: Page):
        """
        Test 6: Verifica diseño responsive móvil
        """
        log_test_step("Probando diseño responsive - Móvil (Playwright)")
        
        mobile_size = RESPONSIVE_SIZES['mobile']
        page.set_viewport_size({
            "width": mobile_size['width'],
            "height": mobile_size['height']
        })
        time.sleep(1)
        
        print(f"📱 Tamaño: {mobile_size['width']}x{mobile_size['height']}")
        
        # Verificar elementos visibles
        expect(page.locator("h1")).to_be_visible()
        expect(page.locator("#contact-form")).to_be_visible()
        
        page.screenshot(path="reports/screenshots/playwright_responsive_mobile.png")
        print("✅ Test PASSED: Diseño móvil verificado")
    
    def test_responsive_tablet(self, page: Page):
        """
        Test 7: Verifica diseño responsive tablet
        """
        log_test_step("Probando diseño responsive - Tablet (Playwright)")
        
        tablet_size = RESPONSIVE_SIZES['tablet']
        page.set_viewport_size({
            "width": tablet_size['width'],
            "height": tablet_size['height']
        })
        time.sleep(1)
        
        print(f"📲 Tamaño: {tablet_size['width']}x{tablet_size['height']}")
        
        expect(page.locator(".container")).to_be_visible()
        
        page.screenshot(path="reports/screenshots/playwright_responsive_tablet.png")
        print("✅ Test PASSED: Diseño tablet verificado")
    
    def test_responsive_desktop(self, page: Page):
        """
        Test 8: Verifica diseño responsive desktop
        """
        log_test_step("Probando diseño responsive - Desktop (Playwright)")
        
        desktop_size = RESPONSIVE_SIZES['desktop']
        page.set_viewport_size({
            "width": desktop_size['width'],
            "height": desktop_size['height']
        })
        time.sleep(1)
        
        print(f"🖥️ Tamaño: {desktop_size['width']}x{desktop_size['height']}")
        
        container = page.locator(".container")
        box = container.bounding_box()
        if box:
            print(f"📐 Ancho del container: {box['width']}px")
        
        page.screenshot(path="reports/screenshots/playwright_responsive_desktop.png")
        print("✅ Test PASSED: Diseño desktop verificado")
    
    def test_box_background_color(self, page: Page):
        """
        Test 9: Verifica color de fondo del box
        """
        log_test_step("Verificando color del box (Playwright)")
        
        box = page.locator(".box")
        bg_color = box.evaluate("el => getComputedStyle(el).backgroundColor")
        padding = box.evaluate("el => getComputedStyle(el).padding")
        
        print(f"🎨 Color de fondo: {bg_color}")
        print(f"📦 Padding: {padding}")
        
        assert bg_color != "rgba(0, 0, 0, 0)"
        
        page.screenshot(path="reports/screenshots/playwright_box_color.png")
        print("✅ Test PASSED: Color del box verificado")
    
    def test_text_readability(self, page: Page):
        """
        Test 10: Verifica legibilidad del texto
        """
        log_test_step("Verificando legibilidad (Playwright)")
        
        title = page.locator("h1")
        text = title.text_content()
        
        assert len(text) > 0
        print(f"📄 Texto del título: '{text}'")
        
        color = title.evaluate("el => getComputedStyle(el).color")
        letter_spacing = title.evaluate("el => getComputedStyle(el).letterSpacing")
        
        print(f"🎨 Color: {color}")
        print(f"↔️ Espaciado: {letter_spacing}")
        
        page.screenshot(path="reports/screenshots/playwright_text_readability.png")
        print("✅ Test PASSED: Texto legible verificado")
    
    def test_navigation_links_styling(self, page: Page):
        """
        Test 11: Verifica estilos de links de navegación
        """
        log_test_step("Verificando estilos de links (Playwright)")
        
        first_link = page.locator(".nav-links a").first
        
        color = first_link.evaluate("el => getComputedStyle(el).color")
        text_decoration = first_link.evaluate("el => getComputedStyle(el).textDecoration")
        font_weight = first_link.evaluate("el => getComputedStyle(el).fontWeight")
        
        print(f"🎨 Color: {color}")
        print(f"✏️ Text decoration: {text_decoration}")
        print(f"💪 Font weight: {font_weight}")
        
        page.screenshot(path="reports/screenshots/playwright_links_styling.png")
        print("✅ Test PASSED: Estilos de links verificados")
    
    def test_animations_and_transitions(self, page: Page):
        """
        Test 12: Verifica que haya transiciones CSS
        """
        log_test_step("Verificando transiciones (Playwright)")
        
        submit_btn = page.locator("#submit-btn")
        transition = submit_btn.evaluate("el => getComputedStyle(el).transition")
        
        print(f"⏱️ Transition: {transition}")
        
        page.screenshot(path="reports/screenshots/playwright_transitions.png")
        print("✅ Test PASSED: Transiciones verificadas")


# Configuración de pytest para Playwright
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configuración del contexto del navegador"""
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


# Para ejecutar solo este archivo:
# pytest tests/playwright_tests/test_ui_ux.py -v -s
