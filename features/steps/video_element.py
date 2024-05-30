from behave import *

@given("the user opens the frontpage's menu")
def step_impl(context):
    context.video_element.open_user_menu()

    
@when('the user clicks on the button "{menu_link_text}"')
def step_impl(context, menu_link_text):
    context.video_element.click_menu_linktext(menu_link_text)
    
@then('a new page with the headline "{video_page_headline}" opens up')
def step_impl(context, video_page_headline):
    context.video_element.verify_video_list(video_page_headline)

@step('this page has a list of "{number_of_links}" links to certain videos')
def step_impl(context, number_of_links):
    context.video_element.verify_number_of_links(number_of_links)    
    
@step('the page has the tab-title "{tab_title}"')
def step_impl(context, tab_title):
    context.video_element.verfiy_tab_title(tab_title)

@when('the user clicks on one of the video-links')
def step_impl(context):
    context.video_element.click_video_link()

@then('a new page with the according embedded Video opens up')
def step_impl(context):
    context.video_element.validate_video_iframe_open_up()
    
@when('the user clicks on the red play-button on the video')
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
    
@when('the user clicks on the video-menu-button on the left top of the page')
def step_impl(context):
    context.video_element.click_video_list_button()    

@then('the page with the headline "{video_page_headline}" opens up again')
def step_impl(context, video_page_headline):
    context.video_element.verify_video_list(video_page_headline)

@when('the user activates the main-menu-button on the left top of the page')
def step_impl(context):
    context.video_element.click_return_button()

@then('the frontpage of the app is opened up with the headline "{front_page_headline}"')
def step_impl(context, front_page_headline):
     context.video_element.validate_frontapge_headline(front_page_headline)