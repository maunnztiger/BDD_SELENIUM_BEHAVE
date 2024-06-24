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
        self.page_link_xpath = "/html/body/div/a"
        self.slide_show_document_title_xpath = "/html/head/meta[1]"
        self.slide_show_first_image_xpath = "//image[@clip-path='url(#p.1)']"
        self.slide_no_field_xpath = "//*[@id=':l']"
        self.progress_slide_up_button_xpath = "/html/body/div[2]/div[1]/div[1]/div[3]"
        self.progress_slide_down_button_xpath = "/html/body/div[2]/div[1]/div[1]/div[1]"
              
    def open_frontpage_menu(self):
        element = self.libs.get_element_by_xpath(self.driver, self.menu_button_xpath)
        element.click()
        sleep(1)
    
    def click_menu_point(self, menu_point):
        element = self.libs.get_element_by_linktext(self.driver, menu_point)
        element.click()
        sleep(1)
    
    def clicking_link(self):
        element = self.libs.get_element_by_xpath(self.driver, self.page_link_xpath)
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
        sleep(1)
       
    def verify_first_aria_label(self, first_aria_label):
        frame1 = self.driver.find_element(by=By.XPATH, value='/html/body/div/iframe')
        self.driver.switch_to.frame(frame1)
        sleep(2)
        image =self.driver.find_element(by=By.TAG_NAME, value='image' )
        image_label = image.get_attribute('aria-label')
        assert first_aria_label == image_label
        sleep(1)
    
    def verify_first_slide_page_number(self, first_page_number):
        slide_no_field = self.libs.get_element_by_xpath(self.driver, self.slide_no_field_xpath)
        slide_no = slide_no_field.text
        print(slide_no, first_page_number)
        assert slide_no == first_page_number

    def click_the_right_arrow(self):
        element = self.libs.get_element_by_xpath(self.driver, "//div[@class='punch-viewer-navbar-next goog-inline-block goog-flat-button']")
        element.click()
        sleep(1)
    
    def verify_second_aria_label(self, second_aria_label):
        image = self.driver.find_element(by=By.TAG_NAME, value='image' )
        image_label = image.get_attribute('aria-label')
        assert image_label == second_aria_label
        sleep(1)
    
    def veryify_second_slide_page_number(self, second_page_number): 
        slide_no_field = self.libs.get_element_by_xpath(self.driver, self.slide_no_field_xpath)
        slide_no = slide_no_field.text
        assert slide_no == second_page_number
        sleep(1)
        
    def click_left_arrow_button(self):
        button = self.libs.get_element_by_xpath(self.driver, "//div[@class='punch-viewer-navbar-prev goog-inline-block goog-flat-button']")
        button.click()
        sleep(1)
    
    def verify_first_slide_page_reload(self, first_aria_label):
        image = self.driver.find_element(by=By.TAG_NAME, value='image' )
        image_label = image.get_attribute('aria-label')
        assert image_label == first_aria_label
        sleep(1)        
        
    def verify_first_slide_page_number(self, first_page_number):
        slide_no_field = self.libs.get_element_by_xpath(self.driver, self.slide_no_field_xpath)
        slide_no = slide_no_field.text
        assert slide_no == first_page_number
             