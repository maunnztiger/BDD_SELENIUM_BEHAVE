import json
import time
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from Pages.basePage import BasePage
from Pages.tutorialPage import TutorialPage
from Pages.table_contentPage import TableContentPage


data = json.load(open("Ressources/config.json"))

# This environment page is used as hooks page. Here we can notice that we have used before, after hooks along side with some step hooks.

def before_scenario(context, scenario):
    context.driver = webdriver.Firefox()
    time.sleep(5)
    basepage = BasePage(context.driver)
    context.tutorialPage = TutorialPage(basepage)
    context.table_content = TableContentPage(basepage)
    context.stepid = 1
    context.driver.get(data["DEXTERSLAB_URL"])
    context.driver.maximize_window()
    context.driver.implicitly_wait(3)
    

  
def after_scenario(context, scenario):
    context.driver.quit()    
    