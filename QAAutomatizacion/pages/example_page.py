"""
Ejemplo de implementación de Page Object para una página específica
Este es un ejemplo que puedes usar como plantilla para las páginas de tus compañeros
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ExamplePage(BasePage):
    """
    Clase que representa una página de ejemplo
    Define todos los locators y acciones específicas de esta página
    """
    
    # ========================================================================
    # LOCATORS - Identificadores de elementos de la página
    # ========================================================================
    
    # Header
    TITLE = (By.TAG_NAME, "h1")
    SUBTITLE = (By.CLASS_NAME, "subtitle")
    
    # Formulario
    INPUT_NAME = (By.ID, "name")
    INPUT_EMAIL = (By.ID, "email")
    INPUT_MESSAGE = (By.ID, "message")
    BUTTON_SUBMIT = (By.ID, "submit-btn")
    
    # Resultados
    SUCCESS_MESSAGE = (By.ID, "success-message")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")
    
    # Navegación
    LINK_HOME = (By.LINK_TEXT, "Home")
    LINK_ABOUT = (By.LINK_TEXT, "About")
    
    # Botones de acción
    BUTTON_SHOW_ALERT = (By.ID, "show-alert")
    BUTTON_CHANGE_COLOR = (By.ID, "change-color")
    
    # Elementos de UI
    BOX_CONTAINER = (By.CLASS_NAME, "box")
    LIST_ITEMS = (By.CSS_SELECTOR, "ul.items li")
    
    # ========================================================================
    # ACCIONES - Métodos que interactúan con la página
    # ========================================================================
    
    def get_page_title_text(self):
        """
        Obtiene el texto del título de la página
        
        Returns:
            str: Texto del título
        """
        return self.get_text(self.TITLE)
    
    def get_subtitle_text(self):
        """
        Obtiene el texto del subtítulo
        
        Returns:
            str: Texto del subtítulo
        """
        return self.get_text(self.SUBTITLE)
    
    def fill_contact_form(self, name, email, message):
        """
        Llena el formulario de contacto
        
        Args:
            name (str): Nombre
            email (str): Email
            message (str): Mensaje
        """
        self.type_text(self.INPUT_NAME, name)
        self.type_text(self.INPUT_EMAIL, email)
        self.type_text(self.INPUT_MESSAGE, message)
    
    def submit_form(self):
        """
        Hace click en el botón de enviar formulario
        """
        self.click(self.BUTTON_SUBMIT)
    
    def get_success_message(self):
        """
        Obtiene el mensaje de éxito
        
        Returns:
            str: Mensaje de éxito
        """
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def is_success_message_displayed(self):
        """
        Verifica si el mensaje de éxito está visible
        
        Returns:
            bool: True si es visible
        """
        return self.is_element_visible(self.SUCCESS_MESSAGE)
    
    def click_home_link(self):
        """
        Hace click en el link de Home
        """
        self.click(self.LINK_HOME)
    
    def click_about_link(self):
        """
        Hace click en el link de About
        """
        self.click(self.LINK_ABOUT)
    
    def click_show_alert(self):
        """
        Hace click en el botón que muestra un alert
        """
        self.click(self.BUTTON_SHOW_ALERT)
    
    def click_change_color(self):
        """
        Hace click en el botón que cambia el color
        """
        self.click(self.BUTTON_CHANGE_COLOR)
    
    def get_box_background_color(self):
        """
        Obtiene el color de fondo del box
        
        Returns:
            str: Color en formato CSS
        """
        return self.get_css_property(self.BOX_CONTAINER, 'background-color')
    
    def get_all_list_items(self):
        """
        Obtiene todos los elementos de una lista
        
        Returns:
            list: Lista de WebElements
        """
        return self.find_elements(self.LIST_ITEMS)
    
    def get_list_items_count(self):
        """
        Cuenta los elementos de la lista
        
        Returns:
            int: Cantidad de elementos
        """
        return len(self.get_all_list_items())
    
    # ========================================================================
    # VALIDACIONES - Métodos para verificar estados
    # ========================================================================
    
    def is_form_displayed(self):
        """
        Verifica si el formulario está visible
        
        Returns:
            bool: True si el formulario es visible
        """
        return (self.is_element_visible(self.INPUT_NAME) and 
                self.is_element_visible(self.INPUT_EMAIL) and
                self.is_element_visible(self.INPUT_MESSAGE))
    
    def is_submit_button_enabled(self):
        """
        Verifica si el botón de submit está habilitado
        
        Returns:
            bool: True si está habilitado
        """
        element = self.find_element(self.BUTTON_SUBMIT)
        return element.is_enabled()
