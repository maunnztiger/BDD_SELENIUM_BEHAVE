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
    
@when('the user clicks on the dark blue Button "Go Back"')
def step_impl(context):
    context.buttons.return_button_click()
    
@then ('the front page with the headline "{headline_text}" appears again')
def step_impl(context, headline_text):
    context.buttons.validate_front_page(headline_text)
    
@step('the title of the tab is again "{tab_title}"')    
def step_impl(context, tab_title):
    context.tutorialPage.tab_validation(tab_title)