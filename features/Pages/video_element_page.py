from features.Pages.base_page import BasePage
from features.Pages.library_page import Library
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep

class VideoElement(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()
        self.driver = context.driver
        self.menu_button_xpath = "//*[@id='menuButton']"
        self.video_iframe_xpath = "/html/body/div/iframe"
        self.number_of_videos = 7
        self.tab_title_xpath = "/html/head/title"
        self.video_source_xpath = "//iframe[@src='https://www.youtube.com/embed/aMxFcrCg4To?si=AlyAcUfmWaw01ltO']" 
        self.Yt_button_xpath = "//button[@class='ytp-large-play-button ytp-button ytp-large-play-button-red-bg']"

    def open_user_menu(self):
        element = self.libs.get_element_by_xpath(self.driver, self.menu_button_xpath)
        element.click()
        sleep(1)
    
    def click_menu_linktext(self, menu_link_text):
        element = self.libs.get_element_by_linktext(self.driver, menu_link_text)
        element.click() 
        sleep(5)
        
    def validate_video_list(self):
        iframes = self.libs.get_elements_by_xpath(self.driver, self.video_iframe_xpath)
        assert str(len(iframes)) == str(self.number_of_videos)
        sleep(1)
        
    def verfiy_tab_title(self, tab_title):
        title = self.driver.title
        assert tab_title in title 
        sleep(2) 
        
    def click_red_play_button(self):    
        frame1 = self.libs.get_element_by_xpath(self.driver, self.video_source_xpath)
        self.driver.switch_to.frame(frame1)
        sleep(2)
        Ytbutton = self.libs.get_element_by_xpath(self.driver, self.Yt_button_xpath)
        Ytbutton.click() #play
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
    
            
        
        
        
                  