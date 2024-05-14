from behave import *


@given('the title of the browser-tab is "{tab_title}"')
def step_impl(context, tab_title):
    context.basic_menu.tab_validation(tab_title)
    
@when('the user clicks the button in the left corner')
def step_impl(context):
    context.basic_menu.click_menu_button()
    
@then('there occurs a blue menu')
def step_impl(context):    
    context.basic_menu.menu_blue_color_validation()

@step('the first menu-point is: "{menupoint}"')
def step_impl(context, menupoint): 
    context.basic_menu.first_menupoint_validation(menupoint)

@step('the second menu-point is: "{menupoint}"')
def step_impl(context, menupoint):
    context.basic_menu.second_menupoint_validation(menupoint)
    
@step('the third menu-point is: "{menupoint}"')
def step_impl(context, menupoint):
    context.basic_menu.third_menupoint_validation(menupoint)
    
@step('the fourth menu-point is: "{menupoint}"')
def step_impl(context, menupoint):
    context.basic_menu.fourth_menupoint_validation(menupoint)   
    
@step('the fifth menu-point is: "{menupoint}"')
def step_impl(context, menupoint):   
    context.basic_menu.fifth_menupoint_validation(menupoint)

@step('the sixth menu-point is: "{menupoint}"')
def step_impl(context, menupoint): 
    context.basic_menu.sixth_menupoint_validation(menupoint)
    
@step('the seventh menu-point is: "{menupoint}"')
def step_impl(context, menupoint): 
    context.basic_menu.seventh_menupoint_validation(menupoint)    
        
@when('the user clicks on the menu button again')
def step_impl(context):
    context.basic_menu.click_menu_button()
 
@then('the menu dissapears again')
def step_impl(context):    
    context.basic_menu.menu_disappears_validation()

