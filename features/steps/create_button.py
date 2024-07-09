from behave import *

@given('the title of the tab will still be "{tab_title}"')
def step_impl(context, tab_title):
    context.basic_menu.tab_validation(tab_title)
    
@when('the user clicks on the menu on the front page')
def step_impl(context):
    context.basic_menu.click_menu_button()
    
@step('the user clicks on the menu-link "{menu_point}"') 
def step_impl(context, menu_point):
    context.return_button.click_on_menupoint(menu_point)
    
@then('the page "{headline_text}" opens up again')
def step_impl(context, headline_text):
    context.return_button.validate_headline_text(headline_text)
    
@step('the title of the tab is again"{tab_title}"')
def step_impl(context, tab_title):
    context.return_button.validate_tab_title(tab_title) 
    
@when('the user clicks on the button "Create Record"')
def step_impl(context):
    context.create_button.create_button_click()
    
@then('a Popup Window is openning up with the headline "{popup_headline}"')
def step_impl(context, popup_headline):
     context.create_button.verify_headline_text(popup_headline)   

@step('there is a textfield with the label "{id_label_text}"')    
def step_impl(context, id_label_text):
    context.create_button.verify_id_label_text(id_label_text)   
    
@step('there is a second textfield with the label "{aspekt_label_text}"')
def step_impl(context, aspekt_label_text):
    context.create_button.verify_aspekt_label_text(aspekt_label_text)   
 
@step('there is a third textfield with the label "{value_label_text}"')
def step_impl(context, value_label_text):
    context.create_button.verify_value_label_text(value_label_text)
       
@step('below the textfields there is a button "{create_button_text}"')
def step_impl(context, create_button_text):
    context.create_button.validate_create_button(create_button_text)
    
@step('there is a "{cancel_button_text}" button')
def step_impl(context, cancel_button_text):
    context.create_button.validate_cancel_button(cancel_button_text)
    
@when('the user adds a Number that is 1 greater than last row ID to the Id-textfield')
def step_impl(context):
    context.create_button.id_textfield_input()

@step('adds the text-value "{aspekt_input_text}" to the Aspekt-textfield')     
def step_impl(context, aspekt_input_text):
    context.create_button.aspect_textfield_input(aspekt_input_text)
 
@step('adds the percentage "{value_input_text}" to the Value-textfield')
def step_impl(context, value_input_text):
    context.create_button.value_textfield_input(value_input_text)

@step('clicks on the Button "Create Record"')
def step_impl(context):
    context.create_button.cause_creating_record()

@then('the Popup is no longer diplayed on the page')
def step_impl(context):
    context.create_button.popup_is_not_displayed()

@step('after two seconds the new text-entry appears at the bottom of the table')
def step_impl(context):
    context.create_button.validate_new_rows_number()
    
@step('the last row "Id"-column has now new Id-text-entry')
def step_impl(context):
    context.create_button.validate_last_row_id_column_text_entry()
    
@step('the last row "Aspekt"-column has now the text-entry: "{aspekt_text_entry}"')
def step_impl(context, aspekt_text_entry):
    context.create_button.validate_last_row_aspekt_column_text_entry(aspekt_text_entry)

@step('the last row "Value"-column has now the text-entry: "{value_text_entry}"')
def step_impl(context, value_text_entry):
    context.create_button.validate_last_row_value_column_text_entry(value_text_entry)  
    
@when('the user clicks on the trash-button on the right of the entry-row')
def step_impl(context):
    context.create_button.click_on_trash_button()

@step('the user accepts the alert that is poping up')
def step_impl(context):
    context.create_button.accept_alert_box()

@then('the according entry will be deleted from the table')       
def step_impl(context):
    context.create_button.validate_deleted_rows_disapears() 