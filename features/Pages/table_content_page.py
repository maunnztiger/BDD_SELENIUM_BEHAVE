import json
from time import sleep
from features.Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from features.Pages.library_page import Library


class TableContentPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()
        
        self.rows_xpath = "//tbody/tr"
        self.menu_button_element_id = "menuButton"
        self.menu_point_link_text = "Men in Homeoffice Data"
        self.headline_id = "headline"
        self.dropdown_selection_xpath = "/html/body/div[4]/div[1]/label/select/option[3]"
        self.searchbar_label_xpath ="/html/body/div[4]/div[2]/label"
        self.label_text = "Search:"
        self.return_button_xpath = "//*[@id='returnButton']"
        self.create_button_xpath = "/html/body/div[3]/p/button"
        self.table_id_xpath = "//table[@id='data_men']"
        self.table_row_xpath = "/html/body/div[4]/table/tbody/tr"
        self.cols_xpath ="/html/body/div[4]/table/thead/tr/th"
        self.first_column_xpath = "/html/body/div[4]/table/thead/tr/th[1]"
        self.second_column_xpath = "/html/body/div[4]/table/thead/tr/th[2]"
        self.third_column_xpath = "/html/body/div[4]/table/thead/tr/th[3]"
        self.first_row_second_column_xpath = "/html/body/div[4]/table/tbody/tr[1]/td[2]"
        self.second_row_second_column_xpath = "/html/body/div[4]/table/tbody/tr[2]/td[2]"
        self.third_row_second_column_xpath = "/html/body/div[4]/table/tbody/tr[3]/td[2]"
        self.last_row_second_column_xpath = "/html/body/div[4]/table/tbody/tr[4]/td[2]"
        self.edit_button_xpath = "/html/body/div[4]/table/tbody/tr[1]/td[4]/i"
        self.delete_button_xpath = "/html/body/div[4]/table/tbody/tr[1]/td[5]/button/i"
        
    
    def click_on_menupoint(self):
        menu_point_link = self.libs.get_element_by_linktext(self.driver, self.menu_point_link_text)
        menu_point_link.click()
        sleep(1)

    def verify_headline(self, headline):
        headline_id = self.libs.get_element_by_id(self.driver, self.headline_id)
        headline_text = headline_id.text
        assert headline_text == headline
        sleep(1)

    def verify_dropdown_selection(self, dropdown_selection_text):
        dropdown_selection = self.libs.get_element_by_xpath(self.driver, self.dropdown_selection_xpath)
        dropdown_text = dropdown_selection.text
        assert dropdown_text == dropdown_selection_text
        sleep(1)


    def validate_searchbar(self):
        searchbar_label = self.libs.get_element_by_xpath(self.driver, self.searchbar_label_xpath)
        searchbar_label_text = searchbar_label.text
        assert searchbar_label_text == self.label_text    
        sleep(1)

    def verify_return_button_name(self, return_button_name):
        return_button = self.libs.get_element_by_xpath(self.driver, self.return_button_xpath)
        return_button_text = return_button.text
        assert return_button_text == return_button_name
        sleep(1)

    def verify_create_button_name(self, create_button_name):
        create_button = self.libs.get_element_by_xpath(self.driver, self.create_button_xpath)
        create_button_text = create_button.text
        assert create_button_text == create_button_name
        sleep(1)

    def verify_number_of_entries(self, number_of_entries):
        rows = self.libs.get_elements_by_xpath(self.driver, self.table_row_xpath)
        assert str(len(rows)) == str(number_of_entries)
        sleep(1)

    def verify_number_of_columns(self, number_of_columns):
        columns = self.libs.get_elements_by_xpath(self.driver, self.cols_xpath)
        assert str(len(columns)) == str(number_of_columns)
        sleep(1)

    def verify_first_column_title(self, first_column_title):
        first_column = self.libs.get_element_by_xpath(self.driver, self.first_column_xpath)
        column_text = first_column.text
        assert column_text == first_column_title
        sleep(1)

    def verify_second_column_title(self, second_column_title):
        second_column = self.libs.get_element_by_xpath(self.driver, self.second_column_xpath)
        column_text = second_column.text
        assert column_text == second_column_title
        sleep(1)

    def verify_third_column_title(self, third_column_title):
        third_column = self.libs.get_element_by_xpath(self.driver, self.third_column_xpath)
        column_text = third_column.text
        assert column_text == third_column_title
        sleep(1)

    def validate_edit_and_delete_button(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.edit_button_xpath)))
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.delete_button_xpath)))
        sleep(1)

    def verify_rows_text_entries(self):
        with open("Ressources/men_in_homeoffice.json", encoding='utf-8') as fh:
            data = json.load(fh)
        
        table_data = self.libs.get_table_data(self.driver, self.rows_xpath)
        table_data_json = json.dumps(table_data, ensure_ascii=False).encode('unicode-escape').decode('utf-8')
        table_data_unicode = table_data_json.encode('utf-8').decode('unicode_escape')
        expected_data_json = json.dumps(data, ensure_ascii=False)
        for i, row_data in enumerate(table_data_unicode):
            assert row_data == expected_data_json[i], f"Die {i}-te Reihe stimmt nicht mit dem erwarteten Datensatz überein."
        
   
