from features.Pages.base_page import BasePage
from features.Pages.library_page import Library
from time import sleep

class Buttons(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()
        

    def click_on_menupoint(self, menu_point):
        element = self.libs.get_element_by_linktext(menu_point)
        element.click()
        sleep(1)
    
        
        