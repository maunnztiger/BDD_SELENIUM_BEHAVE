from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from time import sleep
from features.Pages.basePage import BasePage


# The page contains all the locators and the actions to perform on that web element.
# In this page file we have declared all the locators at the class level and we are using them in the respective methods.


class TutorialPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.menu_button_element_id = "menuButton"
        self.menu_element_id = "menu"
        self.menu_element_CSS_property =  "background-color"
        self.HEX_Color_Value = '#3426fc'
        self.first_menupoint_element_id = "data_general"
        self.second_menupoint_element_id = "data_men"
        self.third_menupoint_element_id = "data_special"
        self.fourth_menupoint_element_id = "data_advantages"
        self.fifth_menupoint_element_id = "data_disadvantages"
        self.sixth_menupoint_element_id = "data_european_comparation"
          
   
    def get_element_by_xpath(self, xpath):
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        return element
   
    def get_elements_by_xpath(self, xpath):
        elements = self.driver.find_elements(by=By.XPATH, value=xpath)
        return elements 
    
    def get_element_by_id(self, id):
        element = self.driver.find_element(by=By.ID, value=id)
        return element
    
    def get_elements_by_id(self, id):
        elements = self.driver.find_elements(by=By.ID, value=id)
        return elements
    
    def get_element_by_linktext(self, linktext):
        element = self.driver.find_element(by=By.LINK_TEXT, value = linktext)
        return element
   
        
    def tab_validation(self, tab_title):
        title = self.driver.title
        assert tab_title in title 
        sleep(2)   
        
    def click_menu_button(self):
        menu_button = self.get_element_by_id(self.menu_button_element_id)
        menu_button.click()
        sleep(1)
    
    def blue_menu_validation(self):
        menu = self.get_element_by_id(self.menu_element_id)
        menu_CSS_color_value = menu.value_of_css_property(self.menu_element_CSS_property)
        menue_background_color = Color.from_string(menu_CSS_color_value)
        HEX_COLOR_BLUE = Color.from_string(self.HEX_Color_Value)
        assert menue_background_color == HEX_COLOR_BLUE
        sleep(1)
        
    def first_menupoint_validation(self, menupoint):
        element = self.get_element_by_id(self.first_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint 
        sleep(1) 
        
    def second_menupoint_validation(self, menupoint):
        element = self.get_element_by_id(self.second_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint
        sleep(1)
    
    def third_menupoint_validation(self, menupoint):
        element = self.get_element_by_id(self.third_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint
        sleep(1)
        
    def fourth_menupoint_validation(self, menupoint):
        element = self.get_element_by_id(self.fourth_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint
        sleep(1)
        
    def fifth_menupoint_validation(self, menupoint):
        element = self.get_element_by_id(self.fifth_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint
        sleep(1)
        
    def sixth_menupoint_validation(self, menupoint):
        element = self.get_element_by_id(self.sixth_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint
        sleep(1)
    
    def menu_disappears_validation(self):
        try:
            menu = self.get_elements_by_id(self.menu_element_id)
            assert len(menu) > 0, "Menu Element has disappeared"
            self.driver.close()
        except:
            self.driver.close()
            assert False, "Menu Element is still visilble"    
            
                             