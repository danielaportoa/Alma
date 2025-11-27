"""
Clase base para implementar el patrón Page Object Model (POM)
Todas las páginas heredan de esta clase base
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.config import EXPLICIT_WAIT


class BasePage:
    """
    Clase base que proporciona funcionalidad común para todas las páginas
    """
    
    def __init__(self, driver):
        """
        Inicializa la página base
        
        Args:
            driver: Instancia de WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
    
    def open_url(self, url):
        """
        Navega a una URL específica
        
        Args:
            url (str): URL a la que navegar
        """
        self.driver.get(url)
    
    def find_element(self, locator):
        """
        Encuentra un elemento
        
        Args:
            locator (tuple): Tupla (By.TYPE, 'value')
            
        Returns:
            WebElement: Elemento encontrado
        """
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        """
        Encuentra múltiples elementos
        
        Args:
            locator (tuple): Tupla (By.TYPE, 'value')
            
        Returns:
            list: Lista de elementos encontrados
        """
        return self.driver.find_elements(*locator)
    
    def wait_for_element_visible(self, locator, timeout=None):
        """
        Espera a que un elemento sea visible
        
        Args:
            locator (tuple): Tupla (By.TYPE, 'value')
            timeout (int): Tiempo máximo de espera
            
        Returns:
            WebElement: Elemento visible
        """
        wait_time = timeout or EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator, timeout=None):
        """
        Espera a que un elemento sea clickeable
        
        Args:
            locator (tuple): Tupla (By.TYPE, 'value')
            timeout (int): Tiempo máximo de espera
            
        Returns:
            WebElement: Elemento clickeable
        """
        wait_time = timeout or EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def click(self, locator):
        """
        Hace click en un elemento
        
        Args:
            locator (tuple): Tupla (By.TYPE, 'value')
        """
        element = self.wait_for_element_clickable(locator)
        element.click()
    
    def type_text(self, locator, text):
        """
        Escribe texto en un elemento
        
        Args:
            locator (tuple): Tupla (By.TYPE, 'value')
            text (str): Texto a escribir
        """
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """
        Obtiene el texto de un elemento
        
        Args:
            locator (tuple): Tupla (By.TYPE, 'value')
            
        Returns:
            str: Texto del elemento
        """
        element = self.wait_for_element_visible(locator)
        return element.text
    
    def is_element_visible(self, locator):
        """
        Verifica si un elemento es visible
        
        Args:
            locator (tuple): Tupla (By.TYPE, 'value')
            
        Returns:
            bool: True si es visible, False si no
        """
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
    
    def get_page_title(self):
        """
        Obtiene el título de la página
        
        Returns:
            str: Título de la página
        """
        return self.driver.title
    
    def get_current_url(self):
        """
        Obtiene la URL actual
        
        Returns:
            str: URL actual
        """
        return self.driver.current_url
    
    def scroll_to_element(self, locator):
        """
        Hace scroll hasta un elemento
        
        Args:
            locator (tuple): Tupla (By.TYPE, 'value')
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def get_element_attribute(self, locator, attribute):
        """
        Obtiene un atributo de un elemento
        
        Args:
            locator (tuple): Tupla (By.TYPE, 'value')
            attribute (str): Nombre del atributo
            
        Returns:
            str: Valor del atributo
        """
        element = self.find_element(locator)
        return element.get_attribute(attribute)
    
    def get_css_property(self, locator, property_name):
        """
        Obtiene una propiedad CSS de un elemento
        
        Args:
            locator (tuple): Tupla (By.TYPE, 'value')
            property_name (str): Nombre de la propiedad
            
        Returns:
            str: Valor de la propiedad
        """
        element = self.find_element(locator)
        return element.value_of_css_property(property_name)
