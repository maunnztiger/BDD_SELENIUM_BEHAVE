
from time import sleep
from features.Pages.base_page import BasePage
from features.Pages.library_page import Library
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class BasicMenuPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()
        self.menu_element_id = "menu"
        self.menu_button_element_id = "menuButton"
        self.menu_element_CSS_property =  "background-color"
        self.HEX_Color_Value = '#3426fc'
        
        self.first_menupoint_element_id = "data_general"
        self.second_menupoint_element_id = "data_men"
        self.third_menupoint_element_id = "data_special"
        self.fourth_menupoint_element_id = "data_advantages"
        self.fifth_menupoint_element_id = "data_disadvantages"
        self.sixth_menupoint_element_id = "data_european_comparation"
        self.seventh_menupoint_element_id = "video_list"
        self.eigth_menupoint_element_id = "text_resources"
        
    def tab_validation(self, tab_title):
        title = self.driver.title
        assert tab_title in title 
        sleep(2)   
        
    def click_menu_button(self):
        menu_button = self.libs.get_element_by_id(self.driver, self.menu_button_element_id)
        menu_button.click()
        sleep(1)
    
    def menu_blue_color_validation(self):
        menu_element = self.libs.get_element_by_id(self.driver, self.menu_element_id)
        css_value = self.libs.get_value_of_css_property(menu_element, self.menu_element_CSS_property)
        color_string_1 = self.libs.get_color_string(css_value)
        color_string_2 = self.libs.get_color_string(self.HEX_Color_Value)
        try:
            assert color_string_1 == color_string_2, "Color is identical to CSS Property"
        except: False, "Colors does not match"    
        sleep(1)
        
    def first_menupoint_validation(self, menupoint_text):
        first_menu_point = self.libs.get_element_by_id(self.driver, self.first_menupoint_element_id)
        menu_point_text = first_menu_point.text
        assert menu_point_text == menupoint_text 
        sleep(1) 
        
    def second_menupoint_validation(self, menupoint_text):
        second_menu_point = self.libs.get_element_by_id(self.driver, self.second_menupoint_element_id)
        menu_point_text = second_menu_point.text
        assert menu_point_text == menupoint_text
        sleep(1)
    
    def third_menupoint_validation(self, menupoint_text):
        third_menu_point = self.libs.get_element_by_id(self.driver, self.third_menupoint_element_id)
        menu_point_text = third_menu_point.text
        assert menu_point_text == menupoint_text
        sleep(1)
        
    def fourth_menupoint_validation(self, menupoint_text):
        fourth_menu_point = self.libs.get_element_by_id(self.driver, self.fourth_menupoint_element_id)
        menu_point_text = fourth_menu_point.text
        assert menu_point_text == menupoint_text
        sleep(1)
        
    def fifth_menupoint_validation(self, menupoint_text):
        fifth_menu_point = self.libs.get_element_by_id(self.driver, self.fifth_menupoint_element_id)
        menu_point_text = fifth_menu_point.text
        assert menu_point_text == menupoint_text
        sleep(1)
        
    def sixth_menupoint_validation(self, menupoint_text):
        sixth_menu_point = self.libs.get_element_by_id(self.driver, self.sixth_menupoint_element_id)
        menu_point_text = sixth_menu_point.text
        assert menu_point_text == menupoint_text
        sleep(1)
    
    def seventh_menupoint_validation(self, menupoint_text):
        seventh_menu_point = self.libs.get_element_by_id(self.driver, self.seventh_menupoint_element_id)
        menu_point_text = seventh_menu_point.text
        assert menu_point_text == menupoint_text
        sleep(1)
        
    def eigth_menupoint_validation(self, menupoint_text):
        eigth_menu_point = self.libs.get_element_by_id(self.driver, self.eigth_menupoint_element_id)
        menu_point_text = eigth_menu_point.text
        assert menu_point_text == menupoint_text
        sleep(1)
        
    def menu_disappears_validation(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.ID, self.menu_element_id)))
        except:
            TimeoutException, "Element is still visible"
