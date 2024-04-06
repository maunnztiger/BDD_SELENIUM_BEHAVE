from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

class Library:

    
    def get_element_by_xpath(self, driver, xpath):
        element = driver.find_element(by=By.XPATH, value=xpath)
        return element
   
    def get_elements_by_xpath(self, driver, xpath):
        elements = driver.find_elements(by=By.XPATH, value=xpath)
        return elements 
    
    def get_element_by_id(self, driver, id):
        element = driver.find_element(by=By.ID, value=id)
        return element
    
    def get_elements_by_id(self, driver,  id):
        elements = driver.find_elements(by=By.ID, value=id)
        return elements
    
    def get_element_by_linktext(self, driver,  linktext):
        element = driver.find_element(by=By.LINK_TEXT, value = linktext)
        return element 
    
    def get_value_of_css_property(self, element, css_property):
        value = element.value_of_css_property(css_property)
        return value
    
    def get_color_string(self, value):
        color_string = Color.from_string(value)
        return color_string
        