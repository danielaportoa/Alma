"""
PRUEBAS DE FUNCIONALIDAD CON PLAYWRIGHT
Tests que verifican que la página funciona correctamente usando Playwright
"""

import pytest
import time
from playwright.sync_api import Page, expect
from utils.helpers import take_screenshot, log_test_step
from config.config import TEST_PAGE_URL


class TestFunctionalityPlaywright:
    """
    Suite de pruebas de funcionalidad usando Playwright
    Verifica que todos los elementos interactivos funcionen correctamente
    """
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """
        Setup que se ejecuta ANTES de cada prueba
        Playwright maneja automáticamente la creación del navegador
        """
        self.page = page
        
        log_test_step("Navegando a la página de prueba")
        page.goto(TEST_PAGE_URL)
        time.sleep(1)
        
        yield
        
        time.sleep(1)  # Pausa antes de cerrar
    
    def test_page_title(self, page: Page):
        """
        Test 1: Verifica que el título de la página sea correcto
        """
        log_test_step("Verificando el título de la página (Playwright)")
        
        # Obtener el título
        title = page.title()
        print(f"📄 Título encontrado: {title}")
        
        # Verificar que contenga texto esperado
        assert "Página de Prueba QA" in title
        
        page.screenshot(path="reports/screenshots/playwright_page_title.png")
        print("✅ Test PASSED: Título verificado correctamente")
    
    def test_form_submission(self, page: Page):
        """
        Test 2: Verifica que el formulario se pueda enviar correctamente
        """
        log_test_step("Probando envío de formulario (Playwright)")
        
        # Llenar el formulario
        page.fill("#name", "María García")
        page.fill("#email", "maria@test.com")
        page.fill("#message", "Mensaje de prueba con Playwright")
        
        print("✍️ Formulario llenado")
        time.sleep(1)
        
        # Enviar el formulario
        page.click("#submit-btn")
        print("📤 Formulario enviado")
        
        # Esperar a que aparezca el mensaje de éxito
        success_msg = page.locator("#success-message")
        expect(success_msg).to_be_visible(timeout=10000)
        
        # Verificar el texto
        expect(success_msg).to_contain_text("exitosamente")
        
        page.screenshot(path="reports/screenshots/playwright_form_success.png")
        print("✅ Test PASSED: Formulario enviado exitosamente")
    
    def test_navigation_links(self, page: Page):
        """
        Test 3: Verifica que los links de navegación existan
        """
        log_test_step("Verificando links de navegación (Playwright)")
        
        # Buscar todos los links
        links = page.locator(".nav-links a")
        count = links.count()
        
        print(f"🔗 Links encontrados: {count}")
        assert count >= 3
        
        # Verificar textos
        for i in range(count):
            text = links.nth(i).text_content()
            print(f"   - {text}")
        
        # Hacer click en el primer link
        links.first.click()
        time.sleep(0.5)
        
        page.screenshot(path="reports/screenshots/playwright_nav_links.png")
        print("✅ Test PASSED: Links de navegación verificados")
    
    def test_alert_functionality(self, page: Page):
        """
        Test 4: Verifica que el botón de alerta funcione
        """
        log_test_step("Probando funcionalidad de alerta (Playwright)")
        
        # Configurar handler para el diálogo
        dialog_message = []
        
        def handle_dialog(dialog):
            dialog_message.append(dialog.message)
            print(f"💬 Texto de alerta: {dialog.message}")
            dialog.accept()
        
        page.on("dialog", handle_dialog)
        
        # Hacer click en el botón de alerta
        page.click("#show-alert")
        print("🔔 Botón de alerta presionado")
        
        time.sleep(1)
        
        # Verificar que se mostró la alerta
        assert len(dialog_message) > 0
        assert "alerta" in dialog_message[0].lower()
        
        print("✅ Test PASSED: Alerta manejada correctamente")
    
    def test_color_change_button(self, page: Page):
        """
        Test 5: Verifica que el botón de cambiar color funcione
        """
        log_test_step("Probando cambio de color del box (Playwright)")
        
        box = page.locator(".box")
        
        # Obtener color inicial
        initial_color = box.evaluate("element => getComputedStyle(element).backgroundColor")
        print(f"🎨 Color inicial: {initial_color}")
        
        page.screenshot(path="reports/screenshots/playwright_color_before.png")
        
        # Hacer click en el botón
        page.click("#change-color")
        print("🖱️ Botón presionado")
        time.sleep(1)
        
        # Obtener nuevo color
        new_color = box.evaluate("element => getComputedStyle(element).backgroundColor")
        print(f"🎨 Color nuevo: {new_color}")
        
        # Verificar que cambió
        assert initial_color != new_color
        
        page.screenshot(path="reports/screenshots/playwright_color_after.png")
        print("✅ Test PASSED: Color cambió correctamente")
    
    def test_list_items_count(self, page: Page):
        """
        Test 6: Verifica que la lista tenga elementos
        """
        log_test_step("Contando elementos de la lista (Playwright)")
        
        items = page.locator("ul.items li")
        count = items.count()
        
        print(f"📋 Elementos encontrados: {count}")
        assert count >= 3
        
        # Imprimir textos
        for i in range(count):
            text = items.nth(i).text_content()
            print(f"   {i+1}. {text}")
        
        page.screenshot(path="reports/screenshots/playwright_list_items.png")
        print("✅ Test PASSED: Lista verificada correctamente")
    
    def test_form_validation(self, page: Page):
        """
        Test 7: Verifica la validación del formulario
        """
        log_test_step("Probando validación de formulario (Playwright)")
        
        # Intentar enviar formulario vacío
        page.click("#submit-btn")
        print("📤 Intentando enviar formulario vacío")
        
        time.sleep(1)
        
        # Verificar que NO aparece el mensaje de éxito
        success_msg = page.locator("#success-message")
        expect(success_msg).not_to_be_visible()
        
        page.screenshot(path="reports/screenshots/playwright_validation.png")
        print("✅ Test PASSED: Validación funcionando")
    
    def test_input_fields_interactivity(self, page: Page):
        """
        Test 8: Verifica que se pueda escribir en los campos
        """
        log_test_step("Probando interactividad de campos (Playwright)")
        
        test_data = {
            '#name': 'Test Playwright User',
            '#email': 'playwright@test.com',
            '#message': 'Mensaje automatizado con Playwright'
        }
        
        for selector, value in test_data.items():
            page.fill(selector, value)
            actual = page.input_value(selector)
            assert actual == value
            print(f"✍️ Campo '{selector}': {value} ✓")
        
        time.sleep(1)
        page.screenshot(path="reports/screenshots/playwright_inputs.png")
        print("✅ Test PASSED: Todos los campos son interactivos")
    
    def test_button_clickable(self, page: Page):
        """
        Test 9: Verifica que los botones sean clickeables
        """
        log_test_step("Verificando botones clickeables (Playwright)")
        
        buttons = [
            "#submit-btn",
            "#show-alert",
            "#change-color"
        ]
        
        for button_id in buttons:
            button = page.locator(button_id)
            expect(button).to_be_enabled()
            print(f"✅ Botón '{button_id}': Clickeable")
        
        page.screenshot(path="reports/screenshots/playwright_buttons.png")
        print("✅ Test PASSED: Botones verificados")
    
    def test_page_has_content(self, page: Page):
        """
        Test 10: Verifica que la página tenga contenido
        """
        log_test_step("Verificando contenido de la página (Playwright)")
        
        # Verificar título
        h1 = page.locator("h1")
        expect(h1).to_have_text("🧪 Página de Prueba QA")
        
        # Verificar subtítulo
        subtitle = page.locator(".subtitle")
        expect(subtitle).to_be_visible()
        
        print("✅ Test PASSED: Página tiene contenido esperado")


# Configuración de pytest para Playwright
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Configuración personalizada para el contexto del navegador
    """
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


# Para ejecutar solo este archivo:
# pytest tests/playwright_tests/test_functionality.py -v -s
