from selenium.webdriver.common.by import By
from time import sleep
from features.Pages.basePage import BasePage


class TableContentPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.menu_button_element_id = "menuButton"
        self.menu_point_link_text = "Homeoffice General Statistic"
        self.headline_id = "headline"
        self.dropdown_selection_xpath = "/html/body/div[4]/div[1]/label/select/option[3]"
        self.searchbar_label_xpath ="/html/body/div[4]/div[2]/label"
        self.label_text = "Search:"
        self.return_button_xpath = "//*[@id='returnButton']"
        self.create_button_xpath = "/html/body/div[3]/p/button"
        self.table_id_xpath = "//table[@id='data_general']"
        self.table_row_xpath = "/html/body/div[4]/table/tbody/tr"
        self.cols_xpath ="/html/body/div[4]/table/thead/tr/th"
        self.first_column_xpath = "/html/body/div[4]/table/thead/tr/th[1]"
        self.second_column_xpath = "/html/body/div[4]/table/thead/tr/th[2]"
        self.third_column_xpath = "/html/body/div[4]/table/thead/tr/th[3]"
        self.first_row_second_column_xpath = "/html/body/div[4]/table/tbody/tr[1]/td[2]"
        self.seventh_row__second_column_xpath = "/html/body/div[4]/table/tbody/tr[7]/td[2]"
        self.last_row_second_column_xpath = "/html/body/div[4]/table/tbody/tr[13]/td[2]"
        self.pencil_button_xpath = "/html/body/div[4]/table/tbody/tr[1]/td[4]/i"
        self.delete_button_xpath = "/html/body/div[4]/table/tbody/tr[1]/td[5]/button/i"
        
    def get_element_by_xpath(self, xpath):
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        return element
   
    def get_elements_by_xpath(self, xpath):
        elements = self.driver.find_elements(by=By.XPATH, value=xpath)
        return elements 
    
    def get_element_by_id(self, id):
        element = self.driver.find_element(by=By.ID, value=id)
        return element
    
    def get_element_by_linktext(self, linktext):
        element = self.driver.find_element(by=By.LINK_TEXT, value = linktext)
        return element

    def click_on_menupoint(self):
        menu_point = self.get_element_by_linktext(self.menu_point_link_text)
        menu_point.click()
        sleep(1)

    def verify_headline(self, headline):
        element= self.get_element_by_id(self.headline_id)
        headline_text = element.text
        assert headline_text == headline
        sleep(1)

    def verify_dropdown_selection(self, dropdown_selection):
        element = self.get_element_by_xpath(self.dropdown_selection_xpath)
        dropdown_text = element.text
        assert dropdown_text == dropdown_selection
        sleep(1)


    def validate_searchbar(self):
        element = self.get_element_by_xpath(self.searchbar_label_xpath)
        searchbar_label_text = element.text
        assert searchbar_label_text == self.label_text    
        sleep(1)

    def verify_return_button_name(self, return_button_name):
        element = self.get_element_by_xpath(self.return_button_xpath)
        return_button_text = element.text
        assert return_button_text == return_button_name
        sleep(1)

    def verify_create_button_name(self, create_button_name):
        element = self.get_element_by_xpath(self.create_button_xpath)
        create_button_text = element.text
        assert create_button_text == create_button_name
        sleep(1)

    def verify_number_of_entries(self, number_of_entries):
        rows = self.get_elements_by_xpath(self.table_row_xpath)
        assert str(len(rows)) == str(number_of_entries)
        sleep(1)

    def verify_number_of_columns(self, number_of_columns):
        columns_number = self.get_elements_by_xpath(self.cols_xpath)
        assert str(len(columns_number)) == str(number_of_columns)
        sleep(1)

    def verify_first_column_title(self, first_column_title):
        element = self.get_element_by_xpath(self.first_column_xpath)
        column_text = element.text
        assert column_text == first_column_title
        sleep(1)

    def verify_second_column_title(self, second_column_title):
        element = self.get_element_by_xpath(self.second_column_xpath)
        column_text = element.text
        assert column_text == second_column_title
        sleep(1)

    def verify_third_column_title(self, third_column_title):
        element = self.get_element_by_xpath(self.third_column_xpath)
        column_text = element.text
        assert column_text == third_column_title
        sleep(1)

    def validate_edit_and_delete_button(self):
        self.get_element_by_xpath(self.pencil_button_xpath)
        self.get_element_by_xpath(self.delete_button_xpath)        
        sleep(1)

    def verify_first_row_text_entry(self, text_entry):
        element = self.get_element_by_xpath(self.first_row_second_column_xpath)
        row_text = element.text       
        assert row_text == text_entry     
        sleep(1)

    def verify_seventh_row_text_entry(self, text_entry):
        element = self.get_element_by_xpath(self.seventh_row__second_column_xpath)
        row_text = element.text        
        assert row_text == text_entry
        sleep(1)

    def verify_last_rows_text_entry(self, text_entry):
        element = self.get_element_by_xpath(self.last_row_second_column_xpath)
        row_text = element.text        
        assert row_text == text_entry       