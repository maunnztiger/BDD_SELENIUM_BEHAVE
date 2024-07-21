from features.Pages.base_page import BasePage
from features.Pages.library_page import Library
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
        self.apsekt_textfield_new_text    = "Männer, die prinzipiell kein Homeoffice machen wollen"
        self.value_textfield_new_text     = "2%"
    
    def click_on_edit_button(self):
        # get the textcontent of the row before click the button in this row
        element_1 = self.libs.get_element_by_xpath(self.driver, self.aspekt_column_xpath)
        element_2 = self.libs.get_element_by_xpath(self.driver, self.value_column_xpath)
        self.aspekt_column_textentry = element_1.text
        self.value_column_textentry = element_2.text
        sleep(1)
        self.edit_button = self.libs.get_element_by_xpath(self.driver, self.edit_button_xpath)
        self.edit_button.click()
        sleep(1)
        
    def validate_popup_headline(self, popup_headline):
        element = self.libs.get_element_by_xpath(self.driver, self.popup_headline_xpath)         
        popup_headline_text = element.text
        assert popup_headline_text == popup_headline
        sleep(1)
        
    def verify_aspekt_label_name(self, label_name):
        element = self.libs.get_element_by_xpath(self.driver, self.popup_aspekt_label_xpath)   
        label_text = element.text
        assert label_text == label_name
        sleep(1)
        
    def verify_value_label_name(self, label_name):     
        element = self.libs.get_element_by_xpath(self.driver, self.popup_value_label_xpath)
        label_text = element.text
        assert label_text == label_name
        sleep(1)
    
    def validate_first_button(self, first_button_name):
        element = self.libs.get_element_by_xpath(self.driver, self.popup_save_button_xpath)
        button_textcontent = element.text
        assert button_textcontent == first_button_name
        sleep(1)
    
    def validate_second_button(self, second_button_name):
        element = self.libs.get_element_by_xpath(self.driver, self.popup_cancel_button_xpath)        
        button_textcontent = element.text
        assert button_textcontent == second_button_name
        sleep(1)
        
    def verify_popup_textfields_textentries(self):
        self.aspekt_textfield = self.libs.get_element_by_xpath(self.driver, self.popup_aspekt_textfield_xpath)
        self.value_textfield = self.libs.get_element_by_xpath(self.driver, self.popup_value_textfield_xpath)
        aspekt_textfield_text = self.aspekt_textfield.text
        value_textfield_text = self.value_textfield.text
        try:
            assert aspekt_textfield_text ==  self.aspekt_column_textentry
            assert value_textfield_text  == self.value_column_textentry
        
        except: AssertionError , "textfields do not match"
        sleep(1)
        
    def change_textfield_entries(self):
        self.driver.execute_script("arguments[0].value=''", self.aspekt_textfield)
        self.driver.execute_script("arguments[0].value=''", self.value_textfield)
        self.aspekt_textfield.send_keys(self.apsekt_textfield_new_text)
        self.value_textfield.send_keys(self.value_textfield_new_text)    
        sleep(1)
        
    def save_changes(self, button_name):
        save_button = self.libs.get_element_by_xpath(self.driver, self.popup_save_button_xpath)
        save_button_text = save_button.text    
        try:
            assert save_button_text == button_name
            save_button.click()
            sleep(1)
        except: Exception   
    
    def verify_columns_new_textentries(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.aspekt_column_xpath)))
        aspekt_column = self.libs.get_element_by_xpath(self.driver, self.aspekt_column_xpath)
        value_column = self.libs.get_element_by_xpath(self.driver, self.value_column_xpath)
        aspekt_column_text = aspekt_column.text
        value_column_text = value_column.text
        try:
            assert value_column_text == self.value_textfield_new_text
            assert aspekt_column_text == self.apsekt_textfield_new_text
            sleep(1)
        except: AssertionError, "Textentries do not match"   


    
        
        