from features.Pages.base_page import BasePage
from features.Pages.library_page import Library
from time import sleep

class Buttons(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()
        self.headline_id = "headline"
        self.tab_title = "Men in Homeoffice Statistic"
        self.front_page_headline_xpath = "/html/body/div[2]/h2"
        self.return_button_xpath = "//*[@id='returnButton']"
        
        

    def click_on_menupoint(self, menu_point):
        element = self.libs.get_element_by_linktext(self.driver, menu_point)
        element.click()
        sleep(1)
    
    def validate_headline_text(self, headline_text):
        element = self.libs.get_element_by_id(self.driver, self.headline_id)
        text = element.text
        assert text == headline_text
        sleep(1)
    
    def validate_tab_title(self, tab_title):
        title = self.driver.title
        assert tab_title in title          
        sleep(1)
    
    def return_button_click(self):
        element = self.libs.get_element_by_xpath(self.driver, self.return_button_xpath)
        element.click()
        sleep(1)
        
    def validate_front_page(self, headline_text):    
        element = self.libs.get_element_by_xpath(self.driver, self.front_page_headline_xpath)    
        front_page_headline_text = element.text
        assert front_page_headline_text == headline_text
        sleep(1)
    
    def validate_tab_title(self, tab_title):
        title = self.driver.title
        assert tab_title in title             
        sleep(1)    
        