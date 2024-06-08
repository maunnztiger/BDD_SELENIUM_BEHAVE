from features.Pages.base_page import BasePage
from features.Pages.library_page import Library
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from time import sleep

class SlideShowPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()
        self.driver = context.driver
        self.menu_button_xpath = "//*[@id='menuButton']"
        self.menu_point_link_text = "Slideshows"
        self.page_link_xpath = "/html/body/div/a"
        self.pages_url = "http://www.dexterslab.com:8080/slide_1.html"
        self.slide_show_document_title_xpath = "/html/head/meta[1]"
        self.imgae_xpath = "/html/body/div[2]/div[2]/div/div/div/div/div[3]/svg/g/g/g/image"
        self.first_image_aria_label = "My Project-1.png"
        self.scond_image_aria_label = "My project-2.png"
        
    def open_frontpage_menu(self):
        element = self.libs.get_element_by_xpath(self.driver, self.menu_button_xpath)
        element.click()
        sleep(1)
    
    def click_menu_point(self, menu_point):
        element =self.libs.get_element_by_linktext(self.driver, self.menu_point_link_text)
        element.click()
        sleep(1)
    
    def verify_pages_linkt_text(self, link_text):
        element = self.libs.get_element_by_xpath(self.driver, self.page_link_xpath)
        element_text = element.text
        assert element_text == link_text
        sleep(1)
    
    def verify_slide_show_pages_url(self, slide_show_page_url):
        url = self.driver.current_url 
        assert url == slide_show_page_url
        
                  