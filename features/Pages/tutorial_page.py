
from time import sleep
from features.Pages.base_page import BasePage
from features.Pages.library_page import Library


# The page contains all the locators and the actions to perform on that web element.
# In this page file we have declared all the locators at the class level and we are using them in the respective methods.


class TutorialPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()
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
        self.seventh_menupoint_element_id = "video_list"
      
       
    def tab_validation(self, tab_title):
        title = self.driver.title
        assert tab_title in title 
        sleep(2)   
        
    def click_menu_button(self):
        menu_button = self.libs.get_element_by_id(self.driver, self.menu_button_element_id)
        menu_button.click()
        sleep(1)
    
    def menu_blue_color_validation(self):
        element = self.libs.get_element_by_id(self.driver, self.menu_element_id)
        css_value = self.libs.get_value_of_css_property(element, self.menu_element_CSS_property)
        color_string_1 = self.libs.get_color_string(css_value)
        color_string_2 = self.libs.get_color_string(self.HEX_Color_Value)
        try:
            assert color_string_1 == color_string_2, "Color is identical to CSS Property"
        except: False, "Color does not match to CSS Property"    
        sleep(1)
        
    def first_menupoint_validation(self, menupoint):
        element = self.libs.get_element_by_id(self.driver, self.first_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint 
        sleep(1) 
        
    def second_menupoint_validation(self, menupoint):
        element = self.libs.get_element_by_id(self.driver, self.second_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint
        sleep(1)
    
    def third_menupoint_validation(self, menupoint):
        element = self.libs.get_element_by_id(self.driver, self.third_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint
        sleep(1)
        
    def fourth_menupoint_validation(self, menupoint):
        element = self.libs.get_element_by_id(self.driver, self.fourth_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint
        sleep(1)
        
    def fifth_menupoint_validation(self, menupoint):
        element = self.libs.get_element_by_id(self.driver, self.fifth_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint
        sleep(1)
        
    def sixth_menupoint_validation(self, menupoint):
        element = self.libs.get_element_by_id(self.driver, self.sixth_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint
        sleep(1)
    
    def seventh_menupoint_validation(self, menupoint):
        element = self.libs.get_element_by_id(self.driver, self.seventh_menupoint_element_id)
        menu_button_text = element.text
        assert menu_button_text == menupoint
        sleep(1)
        
    def menu_disappears_validation(self):
        try:
            menu = self.libs.get_elements_by_id(self.driver, self.menu_element_id)
            assert len(menu) > 0, "Menu Element has disappeared"
            self.driver.close()
        except:
            self.driver.close()
            assert False, "Menu Element is still visilble"    
            
                             