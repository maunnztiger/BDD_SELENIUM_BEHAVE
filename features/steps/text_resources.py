from behave import *

@given('the title of the tab is still "{tab_title}" ')
def step_impl(context, tab_title):
    context.basic_menu.tab_validation(tab_title)
    
@when('the user clicks the menuButton on the front page')
def step_impl(context):
    context.video_element.open_user_menu()

@step ('the user clicks on the point "{menu_link_text}"')
def step_impl(context, menu_link_text):
    context.video_element.click_menu_linktext(menu_link_text)

@then('a page on the URL "{page_URL}" opens up')
def step_impl(context, page_URL):
    context.text_resources.validate_page_url(page_URL)

@step('the page shows a dark blue field')
def step_impl(context):
    context.text_resources.validate_field_colour()
    
@step ('in the center of this blue field are two pictures below each other')
def step_impl(context):
    context.text_resources.validate_two_pictures()
    
@when('the user clicks on the upper picture')
def step_impl(context):
    context.text_resources.click_upper_picture()
    
@then('the dark-blue field with the pictures dispappears')
def step_impl(context):
    context.text_resources.verify_blue_container_disappears()
    
@step('an iframe opens up')
def step_impl(context):
    context.text_resources.validate_open_iframe()
    
@step('this iframe contains a text with a Homeoffice Report')
def step_impl(context):
    context.text_resources.validate_pdf_container()
    
@step('this Report has the title: "{text_content}"')
def step_impl(context, text_content):
    context.text_resources.verify_repport_headline_textcontent(text_content)
    
@when('the user clicks on the button "Text Menu" on the left top')
def step_impl(context):
    context.text_resources.click_text_menu()

@then('the iframe dispappears')
def step_impl(context):
    context.text_resources.validate_iframe_disappears()
    
@step('there is the menu with the two pictures again')
def step_impl(context):
    context.text_resources.validate_picture_menu()
    
@when('the user clicks on the second picture below the upper picture')
def step_impl(context):
    context.text_resources.click_second_picture()

@then('the same iframe opens up')
def step_impl(context):
    context.text_resources.validate_open_iframe()
    
@step('this iframe contains an article with the headline "{article_headline}"') 
def step_impl(context, article_headline):
    context.text_resources.verify_article_headline(article_headline)
    
@when('the user clicks on the button "Text Menu" on the left')
def step_impl(context):
    context.text_resources.click_text_menu()

@then('the iframe is disappered here')
def step_impl(context):
    context.text_resources.validate_iframe_disappears()

@step('the user returns to the menu with the two pictures which appears again')
def step_impl(context):
    context.text_resources.validate_picture_menu()
    
@when('the user clicks on the button "Main Menu" on the left top') 
def step_impl(context):
    context.text_resources.click_main_menu_button()
    
@then('the applications opens up the homepage again')
def step_impl(context):
    context.text_resources.verify_frontpages_URL()
    
@step('the headline of the page is "{headline_text}"')
def step_impl(context, headline_text):
    context.text_resources.verify_headline_textcontent(headline_text)

@step('the title ob the tab is "{tab_title}"')
def step_impl(context, tab_title):
    context.text_resources.verify_tab_title(tab_title)

@step('the blue menu-field is closed')
def step_impl(context):
    context.text_resources.validate_blue_menu_is_closed()

@step('on the left corner there exists the button "{main_menu_textcontent}"')
def step_impl(context, main_menu_textcontent):
    context.text_resources.validate_main_menu_button_exists(main_menu_textcontent)