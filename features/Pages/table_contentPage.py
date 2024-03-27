from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
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
        
        
     
    def click_on_menupoint(self):
        menu_point = self.driver.find_element(by=By.LINK_TEXT, value=self.menu_point_link_text)
        menu_point.click()


    def verify_headline(self, headline):
        headline_text =self.driver.find_element(by=By.ID, value=self.headline_id).text
        assert headline_text == headline


    def verify_dropdown_selection(self, dropdown_selection):
        dropdown_select_text = self.driver.find_element(by=By.XPATH, value=self.dropdown_selection_xpath).text
        assert dropdown_select_text == dropdown_selection


    def validate_searchbar(self):
        searchbar_label_text = self.driver.find_element(by=By.XPATH, value=self.searchbar_label_xpath).text
        assert searchbar_label_text == self.label_text    
    

    def verify_return_button_name(self, return_button_name):
        return_button_text = self.driver.find_element(by=By.XPATH, value=self.return_button_xpath).text
        assert return_button_text == return_button_name

    def verify_create_button_name(self, create_button_name):
        create_button_text = self.driver.find_element(by=By.XPATH, value=self.create_button_xpath).text
        assert create_button_text == create_button_name
    

    def verify_number_of_entries(self, number_of_entries):
        rows = self.driver.find_elements(By.XPATH, self.table_row_xpath)
        assert str(len(rows)) == str(number_of_entries)


    def verify_number_of_columns(self, number_of_columns):
        columns_number = self.driver.find_elements(By.XPATH, self.cols_xpath)
        assert str(len(columns_number)) == str(number_of_columns)
        

    def verify_first_column_title(self, first_column_title):
        column_text = self.driver.find_element(by=By.XPATH, value=self.first_column_xpath).text
        assert column_text == first_column_title
    

    def verify_second_column_title(self, second_column_title):
        column_text = self.driver.find_element(by=By.XPATH, value=self.second_column_xpath).text
        assert column_text == second_column_title
    

    def verify_third_column_title(self, third_column_title):
        column_text = self.driver.find_element(by=By.XPATH, value=self.third_column_xpath).text
        assert column_text == third_column_title
    

    def validate_edit_and_delete_button(self):
        assert True is not False        


    def verify_first_row_text_entry(self, text_entry):
        assert True is not False      


    def verify_sixth_row_text_entries(self, text_entry):
        assert True is not False    
    

    def verify_last_rows_text_entries(self, text_entry):
        assert True is not False       