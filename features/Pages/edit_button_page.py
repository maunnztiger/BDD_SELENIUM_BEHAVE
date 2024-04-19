from features.Pages.base_page import BasePage
from features.Pages.library_page import Library
from time import sleep

class EditButton(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()
        self.context = context
        self.aspekt_column_xpath          = "/html/body/div[4]/table/tbody/tr[4]/td[2]"
        self.value_column_xpath           = "/html/body/div[4]/table/tbody/tr[4]/td[3]"
        self.edit_button_xpath            = "/html/body/div[4]/table/tbody/tr[4]/td[4]/i"
        self.popup_headline_xpath         = "/html/body/div[5]/div[1]/h2"
        self.popup_aspekt_label_xpath     = "/html/body/div[5]/div[1]/label[1]"
        self.popup_aspekt_textfield_xpath = "//*[@id='aspect']"
        self.popup_value_label_xpath      = "/html/body/div[5]/div[1]/label[2]"
        self.popup_value_textfield_xpath  = "//*[@id='value']"
        self.popup_save_button_xpath      = "/html/body/div[5]/div[2]/button[1]"
        self.popup_cancel_button_xpath    = "/html/body/div[5]/div[2]/button[2]"
    
    def click_on_edit_button(self):
        # get the textcontent of the row before click the button in this row
        element_1 = self.libs.get_element_by_xpath(self.driver, self.aspekt_column_xpath)
        element_2 = self.libs.get_element_by_xpath(self.driver, self.value_column_xpath)
        self.aspekt_column_textentry = element_1.text
        self.value_column_textentry = element_2.text
        sleep(1)
        edit_button = self.libs.get_element_by_xpath(self.driver, self.edit_button_xpath)
        edit_button.click()
        sleep(1)
        
             