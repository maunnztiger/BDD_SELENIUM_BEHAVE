from features.Pages.base_page import BasePage
from features.Pages.library_page import Library
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from time import sleep

class TextResources(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()
        self.image_container_xpath ="//*[@id='image_container']"
        self.first_image_xpath = "//*[@id='0']"
        self.second_picture_xpath = "//*[@id='1']"
        self.iframe_container_xpath = "//*[@id='iframe_container'']"
        self.report_title_span_xpath = "/html/body/div[1]/div[2]/div[8]/div[2]/div[1]/div[2]/span[1]"
        self.text_menu_button_xpath = "//*[@id='text_list']"
        self.main_menu_button_xpath = "//*[@id='main_menu']"
        self.article_headline_xpath = "/html/body/header/div/div/h1" 
        self.frontpage_main_menu_button_xpath = "//*[@id='menuButton']"
        self.frontpage_headline_xpath = "/html/body/div[2]/h2"
        self.image_container_background_color_css_value = "rgb(18, 44, 82)"
        self.image_container_background_color_css_property = "background-color"
        self.blue_menubox_left_css_property = "left"
        self.blue_menubox_left_css_value = "-250px"
        self.blue_menubox_xpath = "//*[@id='menu']"
        self.blue_menu_button_xpath = "//*[@id='menuButton']"
        self.frontPage_URL = "http://192.168.178.53:5000/index.html"
        
    def validate_page_url(self, page_URL):
        get_url = self.driver.current_url
        assert get_url == page_URL
        sleep(1)
    
    def validate_field_colour(self):
        element = self.libs.get_element_by_xpath(self.driver, self.image_container_xpath)
        field_color = self.libs.get_value_of_css_property(element, self.image_container_background_color_css_property)
        print(field_color)
        assert field_color == self.image_container_background_color_css_value
        sleep(1)
    def validate_two_pictures(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.first_image_xpath )))
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.second_picture_xpath )))
        except: TimeoutException, 'Element is not loaded after 5 Seconds' 
        sleep(1)
        
    def click_upper_picture(self):
        element = self.libs.get_element_by_xpath(self.driver, self.first_image_xpath)
        element.click()
        sleep(1)
        
    def verify_blue_container_disappears(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, self.image_container_xpath)))
        except: TimeoutException, 'Element is still visible'
        sleep(1)
        
    def validate_open_iframe(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.iframe_container_xpath )))
        except: TimeoutException, 'Element is not loaded after 5 Seconds' 
        sleep(1)
        
    def validate_pdf_container(self):
        try:
            iframe = self.libs.get_element_by_xpath(self.driver, self.iframe_container_xpath)
            self.driver.switch_to.frame(iframe)
            sleep(2)
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.report_title_span_xpath)))
        except: TimeoutException, 'Element is not loaded after 5 Seconds' 
        sleep(1)
        
    def verify_repport_headline_textcontent(self, text_content):
        try:
            headline_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.report_title_span_xpath)))
            headline_text = headline_element.text
            assert headline_text == text_content
            self.driver.switch_to.default_content()
            sleep(2)
        except: TimeoutException, 'Element is not loaded after 5 Seconds' 
        
        
        
    def click_text_menu(self):
        menu_button = self.libs.get_element_by_xpath(self.driver, self.text_menu_button_xpath)
        menu_button.click()
        sleep(1)
        
    def validate_iframe_disappears(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, self.iframe_container_xpath)))
        except: TimeoutException, 'Element is still visible'
        sleep(1)
        
    def validate_picture_menu(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.image_container_xpath)))
        except: TimeoutException, 'Element is not loaded after 5 Seconds' 
        sleep(1)
        
    def click_second_picture(self):
        second_picture = self.libs.get_element_by_xpath(self.driver, self.second_picture_xpath)
        second_picture.click()
        sleep(1)
        
    def verify_article_headline(self, article_headline):
        try:
            iframe = self.libs.get_element_by_xpath(self.driver, self.iframe_container_xpath)
            self.driver.switch_to.frame(iframe)
            sleep(2)
            headline = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.article_headline_xpath)))
            headline_text = headline.text
            assert headline_text == article_headline
            self.driver.switch_to.default_content()
            sleep(2)
        except: TimeoutException, 'Element is not loaded after 5 Seconds' 
        
    def click_main_menu_button(self):
        main_manu_button = self.libs.get_element_by_xpath(self.driver, self.main_menu_button_xpath)
        main_manu_button.click()
        sleep(1)
        
    def verify_frontpages_URL(self):
        get_url = self.driver.current_url
        assert get_url == self.frontPage_URL
        sleep(1)
        
    def verify_headline_textcontent(self, headline_text):
        headline = self.libs.get_element_by_xpath(self.driver, self.frontpage_headline_xpath)
        frontpage_headline_text = headline.text
        assert frontpage_headline_text == headline_text
        sleep(1)
        
    def verify_tab_title(self, tab_title):
        title = self.driver.title
        assert tab_title in title 
        sleep(2) 
    
    def validate_blue_menu_is_closed(self):
        menubox = self.libs.get_element_by_xpath(self.driver, self.blue_menubox_xpath)
        postion_left = self.libs.get_value_of_css_property(menubox, self.blue_menubox_left_css_property)
        assert postion_left == self.blue_menubox_left_css_value
        sleep(1)
        
    def validate_main_menu_button_exists(self, main_menu_textcontent):
        menu_button = self.libs.get_element_by_xpath(self.driver, self.blue_menu_button_xpath )
        menu_button_text = menu_button.text
        assert menu_button_text == main_menu_textcontent
        sleep(1)
        