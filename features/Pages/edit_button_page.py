from features.Pages.base_page import BasePage
from features.Pages.library_page import Library
from time import sleep

class EditButton(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()
        "/html/body/div[4]/table/tbody/tr[4]/td[2]"
        "/html/body/div[4]/table/tbody/tr[4]/td[3]"
        "/html/body/div[4]/table/tbody/tr[4]/td[4]/i"
        "/html/body/div[5]/div[1]/h2"
        "/html/body/div[5]/div[1]/label[1]"
        "//*[@id='aspect']"
        "/html/body/div[5]/div[1]/label[2]"
        "//*[@id='value']"
        "/html/body/div[5]/div[2]/button[1]"
        "/html/body/div[5]/div[2]/button[2]"
    
    def click_on_edit_button(self):
        # get the textcontent of the row before click the button in this row
        pass     