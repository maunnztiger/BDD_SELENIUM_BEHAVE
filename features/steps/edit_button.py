from behave import *

@given('the user opens up the page "{headline_text}"')
def step_impl(context, headline_text):
    context.tutorialPage.click_menu_button()
    context.table_content.click_on_menupoint()
    context.table_content.verify_headline(headline_text)

@when('the user clicks on the edit-button at the right end a row of the table')
def step_impl(context):
    context.edit_button.click_on_edit_button()
    
@then('a popup opens up with the headline "{popup_headline}"')
def step_impl(context, popup_headline):
    context.edit_button.validate_popup_headline(popup_headline)
    
@step('the popup has a first label "{label_name}"')
def step_impl(context, label_name):
    context.edit_button.verify_aspekt_label_name(label_name)

@step('the popup has a second label "{label_name}"')
def step_impl(context, label_name):
    context.edit_button.verify_value_label_name(label_name)    
    
@step('there is a "{first_button_name}"-Button below the editor-textfields')     
def step_impl(context, first_button_name):
    context.edit_button.validate_first_button(first_button_name)
    
@step('there is a "{second_button_name}"-Button below the the textfields')
def step_impl(context, second_button_name):
    context.edit_button.validate_second_button(second_button_name)
    
@step('the textcontent of the columns are given in the Popup-textfields')
def step_impl(context):
    context.edit_button.verify_popup_textfields_textentries()
  
@when('the user changes the textcontent of the textfields')
def step_impl(context):
    context.edit_button.change_textfield_entries()

@step('clicks on the button "{button_name}"')
def step_impl(context, button_name):
    context.edit_button.save_changes(button_name)
    
@then('the according row has new textentries in the column "Aspekt"')
def step_impl(context):
    context.edit_button.verify_aspekt_column_new_textentry()  
    
@step('the according row has a new textcontent in the column "Value"')
def step_impl(context):
    context.edit_button.verify_value_column_new_textentry()  