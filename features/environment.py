import json
import os
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.service import Service
from features.Pages.base_page import BasePage
from features.Pages.basic_menu_page import BasicMenuPage
from features.Pages.table_content_page import TableContentPage
from features.Pages.return_button_page import ReturnButton
from features.Pages.create_button_page import CreateButton
from features.Pages.edit_button_page import EditButton
from features.Pages.video_element_page import VideoElement
from features.Pages.slide_show_page import SlideShowPage



data = json.load(open("Ressources/config.json"))

# This environment page is used as hooks page. Here we can notice that we have used before, after hooks along side with some step hooks.

def before_scenario(context, scenario):
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    opts.add_argument("--disable-gpu")
    opts.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    context.driver = webdriver.Firefox(options=opts)
    context.driver.implicitly_wait(60)
    basepage = BasePage(context.driver)
    context.basic_menu = BasicMenuPage(basepage)
    context.table_content = TableContentPage(basepage)
    context.return_button = ReturnButton(basepage)
    context.create_button = CreateButton(basepage)
    context.edit_button = EditButton(basepage)
    context.video_element = VideoElement(basepage)
    context.slide_show = SlideShowPage(basepage)
    context.stepid = 1
    context.driver.get(data["DEXTERSLAB_URL"])
    context.driver.maximize_window()
    context.driver.implicitly_wait(3)
    

  
def after_scenario(context, scenario):
    context.driver.quit()    
    