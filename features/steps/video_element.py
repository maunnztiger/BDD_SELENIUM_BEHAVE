from behave import *

@given("the user opens the frontpage's menu")
def step_impl(context):
    context.video_element.open_user_menu()

    
@when('the user clicks on the button "{menu_link_text}"')
def step_impl(context, menu_link_text):
    context.video_element.click_menu_linktext(menu_link_text)
    
@then('a new page with a list of 7 embedded Youtube-videos opens up')
def step_impl(context):
    context.video_element.validate_video_list()
    
@step('the page has the tab-title "{tab_title}"')
def step_impl(context, tab_title):
    context.video_element.verfiy_tab_title(tab_title)
    
@when('the user clicks on the red play-button on of the videos')
def step_impl(context):
    context.video_element.click_red_play_button()        

@then('the video is played')
def step_impl(context):
    context.video_element.vaildate_video_play()
    
@when('the user presses "{keyboard_key}"-key on the keyboard')
def step_impl(context, keyboard_key):
    context.video_element.press_keyboard_key(keyboard_key)    
    
@then('the video is paused')
def step_impl(context):
    context.video_element.validate_video_is_paused()    
    