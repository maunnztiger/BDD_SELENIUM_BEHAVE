from behave import *


@given('the title of the browser-tab is "{tab_title}"')
def step_impl(context, tab_title):
    context.tutorialPage.tab_validation(tab_title)
    
@when('the user clicks the button in the left corner')
def step_impl(context):
    context.tutorialPage.click_menu_button()
    
@then('there occurs a blue menu')
def step_impl(context):    
    context.tutorialPage.blue_menu_validation()