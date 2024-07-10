from features.Pages.base_page import BasePage
from features.Pages.library_page import Library
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep


class CreateButton(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()
        self.table_rows_xpath = "/html/body/div[4]/table/tbody/tr"
        self.table_last_row_first_column_xpath = "/html/body/div[4]/table/tbody/tr[last()]/td[1]"
        self.table_last_row_second_column_xpath = "/html/body/div[4]/table/tbody/tr[last()]/td[2]"
        self.table_last_row_third_column_xpath = "/html/body/div[4]/table/tbody/tr[last()]/td[3]"
        self.create_button_xpath = "//button[text()='Create Button']"
        self.delete_button_xpath = "/html/body/div[4]/table/tbody/tr[5]/td[5]/button"
        self.save_record_button_xpath = "/html/body/div[7]/div[2]/button[1]"
        self.popup_overlay_xpath = "//*[@id='popup2']"
        self.overlay_css_property = "display"
        self.popup_headline_xpath = "/html/body/div[7]/div[1]/h2"
        self.id_label_xpath = "/html/body/div[7]/div[1]/label[1]"
        self.id_input_xpath ="//*[@id='Id']"
        self.aspekt_label_xpath = "/html/body/div[7]/div[1]/label[2]"
        self.aspekt_input_xpath = "//*[@id='aspect2']"        
        self.value_label_xpath ="/html/body/div[7]/div[1]/label[3]"
        self.value_input_xpath = "//*[@id='value2']"
        self.create_button_xpath ="/html/body/div[7]/div[2]/button[1]"
        self.close_editor_button_xpath ="/html/body/div[7]/div[2]/button[2]"
        
    def create_button_click(self):
        button = self.libs.get_element_by_id(self.driver, 'create_button')
        button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, 'create_button' )))
        self.driver.execute_script("arguments[0].click();", button)
        sleep(2)

    def verify_headline_text(self, popup_headline):   
        element = self.libs.get_element_by_xpath(self.driver, self.popup_headline_xpath)
        headline_text= element.text 
        assert headline_text == popup_headline
        sleep(1)
        
    def verify_id_label_text(self, id_label_text):
        element = self.libs.get_element_by_xpath(self.driver, self.id_label_xpath)       
        label_text =element.text
        assert label_text == id_label_text
        sleep(1)
        
    def verify_aspekt_label_text(self, aspekt_label_text):
        element = self.libs.get_element_by_xpath(self.driver, self.aspekt_label_xpath)
        label_text = element.text
        assert label_text == aspekt_label_text
        sleep(1)
    
    def verify_value_label_text(self, value_label_text):
        element = self.libs.get_element_by_xpath(self.driver, self.value_label_xpath)        
        label_text = element.text
        assert label_text == value_label_text
        sleep(1)
        
    def validate_create_button(self, create_button_text):
        element = self.libs.get_element_by_xpath(self.driver, self.create_button_xpath)    
        button_text = element.text
        assert button_text == create_button_text
        sleep(1)
        
    def validate_cancel_button(self, cancel_button_text):
        element = self.libs.get_element_by_xpath(self.driver, self.close_editor_button_xpath)    
        button_text = element.text
        assert button_text == cancel_button_text
        sleep(1)
        
    def id_textfield_input(self):
        textfield = self.libs.get_element_by_xpath(self.driver,self.id_input_xpath)
        rows = self.libs.get_elements_by_xpath(self.driver, self.table_rows_xpath)
        self.number_of_rows = len(rows)
        
        textfield.send_keys(self.number_of_rows)
        sleep(1)
    
    def aspect_textfield_input(self, aspekt_input_text):
        textfield = self.libs.get_element_by_xpath(self.driver, self.aspekt_input_xpath)
        textfield.send_keys(aspekt_input_text)
        sleep(1)
        
    def value_textfield_input(self, value_input_text):
        textfield = self.libs.get_element_by_xpath(self.driver, self.value_input_xpath)    
        textfield.send_keys(value_input_text)
        sleep(1)
        
    def cause_creating_record(self):
        save_button = self.libs.get_element_by_xpath(self.driver, self.save_record_button_xpath)
        save_button.click()
        sleep(1)

    def popup_is_not_displayed(self):
        WebDriverWait(self.driver, 2).until(EC.invisibility_of_element_located((By.XPATH, self.popup_overlay_xpath)))
        sleep(1)
        
    def validate_new_rows_number(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.table_rows_xpath)))
        rows = self.libs.get_elements_by_xpath(self.driver, self.table_rows_xpath)
        assert len(rows) == (self.number_of_rows+1)
        sleep(1)
    
    def validate_last_row_id_column_text_entry(self):
        last_row = self.libs.get_element_by_xpath(self.driver, self.table_last_row_first_column_xpath)    
        row_text_content = last_row.text
        assert str(row_text_content) == str(self.number_of_rows)
        sleep(1)
    
    def validate_last_row_aspekt_column_text_entry(self, aspekt_text_entry):
        last_row = self.libs.get_element_by_xpath(self.driver, self.table_last_row_second_column_xpath) 
        row_text_content = last_row.text
        assert row_text_content == aspekt_text_entry
        sleep(1)
       
    def validate_last_row_value_column_text_entry(self, value_text_entry):
        last_row = self.libs.get_element_by_xpath(self.driver, self.table_last_row_third_column_xpath) 
        row_text_content = last_row.text
        assert row_text_content == value_text_entry               
        sleep(1)
        
    def click_on_trash_button(self):
        trash_button = self.libs.get_element_by_xpath(self.driver, self.delete_button_xpath)
        trash_button.click()
        sleep(1)
        
    def accept_alert_box(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()    
        sleep(1)
    
    def validate_deleted_rows_disapears(self):
        try:
            WebDriverWait(self.driver, 2
        ).until_not(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/table/tbody/tr[5]')))
        except: TimeoutException, 'Element is still present'    
        