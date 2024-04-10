import json
import time
from selenium import webdriver
from features.Pages.base_page import BasePage
from features.Pages.tutorial_page import TutorialPage
from features.Pages.table_content_page import TableContentPage
from features.Pages.return_button_page import ReturnButton
from features.Pages.create_button_page import CreateButton



data = json.load(open("Ressources/config.json"))

# This environment page is used as hooks page. Here we can notice that we have used before, after hooks along side with some step hooks.

def before_scenario(context, scenario):
    context.driver = webdriver.Firefox()
    time.sleep(5)
    basepage = BasePage(context.driver)
    context.tutorialPage = TutorialPage(basepage)
    context.table_content = TableContentPage(basepage)
    context.return_button = ReturnButton(basepage)
    context.create_button = CreateButton(basepage)
    context.stepid = 1
    context.driver.get(data["DEXTERSLAB_URL"])
    context.driver.maximize_window()
    context.driver.implicitly_wait(3)
    

  
def after_scenario(context, scenario):
    context.driver.quit()    
    