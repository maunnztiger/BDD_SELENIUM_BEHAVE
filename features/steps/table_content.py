from behave import *


@given('the title of the tab is "{tab_title}"')
def step_impl(context, tab_title):
    context.basic_menu.tab_validation(tab_title)
    
@when('the user clicks the menu-button in the left corner')
def step_impl(context):
    context.basic_menu.click_menu_button()
    
@then('there occurs a blue colored menu')
def step_impl(context):    
    context.basic_menu.menu_blue_color_validation()
    
@when('the user clicks on the menupoint "Men in Homeoffice Statistic"') 
def step_impl(context):
    context.table_content.click_on_menupoint()

@then('a page opens with the headline "{headline}"')
def step_impl(context, headline):
    context.table_content.verify_headline(headline)
    
@step('the page has a dropdown in the left corner with selected number of entries shown "{dropdown_selection}"')    
def step_impl(context, dropdown_selection):
    context.table_content.verify_dropdown_selection(dropdown_selection)

@step('in the right corner the page contains a search bar')    
def step_impl(context):
    context.table_content.validate_searchbar()    
    
@step('the page contains a dark blue colored button with the text "{return_button_name}"')
def step_impl(context, return_button_name):
    context.table_content.verify_return_button_name(return_button_name)

@step('the page contains another blue button with the text "{create_button_name}"')
def step_impl(context, create_button_name):
    context.table_content.verify_create_button_name(create_button_name)
    
@step('the page contains a table with "{number_of_entries}" entries')    
def step_impl(context, number_of_entries):
    context.table_content.verify_number_of_entries(number_of_entries)

@step('the table has "{number_of_columns}" columns')    
def step_impl(context,number_of_columns):
    context.table_content.verify_number_of_columns(number_of_columns)
        
@step('the first column has the title "{first_column_title}"')    
def step_impl(context, first_column_title):
    context.table_content.verify_first_column_title(first_column_title)        
    
@step('the second column has the title "{second_column_title}"')    
def step_impl(context, second_column_title):
    context.table_content.verify_second_column_title(second_column_title)      
    
@step('the third column has the title "{third_column_title}"')    
def step_impl(context, third_column_title):
    context.table_content.verify_third_column_title(third_column_title)      
    
@step('the fourth column contains an edit button and a delete-button')
def step_impl(context):
    context.table_content.validate_edit_and_delete_button()        

@step('the the rows have certain text-entries')
def step_impl(context):
    context.table_content.verify_rows_text_entries()      

 