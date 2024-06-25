from features.Pages.base_page import BasePage
from features.Pages.library_page import Library
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from time import sleep

class VideoElement(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()
        self.driver = context.driver
        self.menu_button_xpath = "//*[@id='menuButton']"
        self.video_list_button_xpath = "//*[@id='video_list']"
        self.main_menu_button_xpath = "//*[@id='main_menu']"
        self.frontpage_headline_xpath = "/html/body/div[2]/h2"
        self.video_list_page_headline_xpath ="/html/body/div[1]/h1"
        self.link_container_video_link_elements_xpath = "/html/body/div[3]/div"
        self.video_link_xpath ="//*[@id='0']"
        self.number_of_links = 7
        self.video_source_xpath = "//iframe[@src='https://www.youtube.com/embed/aMxFcrCg4To?si=AlyAcUfmWaw01ltO']"
        self.Yt_button_xpath = "/html/body/div[1]/div/div[4]/button"

    def open_user_menu(self):
        element = self.libs.get_element_by_xpath(self.driver, self.menu_button_xpath)
        element.click()
        sleep(1)
    
    def click_menu_linktext(self, menu_link_text):
        element = self.libs.get_element_by_linktext(self.driver, menu_link_text)
        element.click() 
        sleep(5)
        
    def verify_video_list(self, video_page_headline):
        element = self.libs.get_element_by_xpath(self.driver, self.video_list_page_headline_xpath)
        element_text_content = element.text 
        assert element_text_content == video_page_headline
        sleep(1)
        
    def verfiy_tab_title(self, tab_title):
        title = self.driver.title
        assert tab_title in title 
        sleep(2) 
    
    def verify_number_of_links(self, number_of_links):
        elements = self.libs.get_elements_by_xpath(self.driver, self.link_container_video_link_elements_xpath)
        assert str(len(elements)) == str(number_of_links) 
        sleep(1)
        
    def click_video_link(self):
        element = self.libs.get_element_by_xpath(self.driver, self.video_link_xpath)
        element.click()
        sleep(1)
    
    def validate_video_iframe_open_up(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.video_source_xpath )))
        except: TimeoutException, 'Element is not loaded after 5 Seconds'       # type: ignore
    
    
    def click_red_play_button(self):
        frame1 = self.libs.get_element_by_xpath(self.driver, '/html/body/div[2]/iframe')
        self.driver.switch_to.frame(frame1)
        sleep(2)
        Ytbutton = self.libs.get_element_by_xpath(self.driver, self.Yt_button_xpath)
        Ytbutton = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.Yt_button_xpath )))
        Ytbutton.click()
        sleep(5)
        
    
    def vaildate_video_play(self):
        element = self.libs.get_element_by_xpath(self.driver, "//span[@class='ytp-time-current']")
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        video_current_time = element.text
        assert video_current_time != '0:00'
        sleep(1)
        
    
    def press_keyboard_key(self, keyboard_key):
        ActionChains(self.driver).send_keys(str(keyboard_key)).perform()
        sleep(1)
    
    def validate_video_is_paused(self):
        element = self.libs.get_element_by_xpath(self.driver, "//span[@class='ytp-time-current']")
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        video_current_time_1 = element.text
        sleep(5)
        video_current_time_2 = element.text
        assert video_current_time_1 == video_current_time_2 
    
    def click_video_list_button(self, link_text):
        self.driver.switch_to.default_content()
        button = self.libs.get_element_by_linktext(self.driver, link_text)
        button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
        self.driver.execute_script("arguments[0].click();", button)
        sleep(1)
    
    
    def click_return_button(self):
        button = self.libs.get_element_by_xpath(self.driver, self.main_menu_button_xpath)        
        button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, self.main_menu_button_xpath)))
        self.driver.execute_script("arguments[0].click();", button)
        sleep(1)
        
    def validate_frontpage_headline(self, front_page_headline):
        element = self.libs.get_element_by_xpath(self.driver, self.frontpage_headline_xpath)    
        element_text= element.text
        assert element_text == front_page_headline
    
    
        
                  
