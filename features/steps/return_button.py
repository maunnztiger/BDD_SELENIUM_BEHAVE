from behave import *

@given('the title of the tab is still "{tab_title}"')
def step_impl(context, tab_title):
    context.tutorialPage.tab_validation(tab_title)
    
@when('the user clicks the menu-button on the front page')
def step_impl(context):
    context.tutorialPage.click_menu_button()
    
@step('the user clicks on the menupoint "{menu_point}"') 
def step_impl(context, menu_point):
    context.buttons.click_on_menupoint(menu_point)
    
@then('the page "{headline_text}" opens up')
def step_impl(context, headline_text):
    context.buttons.validate_headline_text(headline_text)
    
@step('the title of the tab is "{tab_title}"')
def step_impl(context, tab_title):
    context.buttons.validate_tab_title(tab_title)        
    
@when('the user clicks on the dark blue Button "{button_1_name}"')
def step_impl(context, button_1_name):
    context.button.click_button(button_1_name)
    
@then ('the front page appears again')
def step_impl(context):
    context.button.validate_front_page()

@step('the front page has the headline "{headline_text}"')
def step_impl(context, headline_text):
    context.buttons.validate_headline_text(headline_text)
    
@step('the title of the tab is again "{tab_title}" ')    
def step_impl(context, tab_title):
    context.tutorialPage.tab_validation(tab_title)