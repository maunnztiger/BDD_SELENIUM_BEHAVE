from behave import *

@given('the user opens the frontpages menu')
def step_impl(context):
    context.slide_show.open_frontpage_menu()
    
@when('the user clicks on the menu-point "{menu_point}"')
def step_impl(context, menu_point):
    context.slide_show.click_menu_point(menu_point)

@then('another page opens up with the link "{link_text}"')
def step_impl(context, link_text):
    context.slide_show.verify_pages_linkt_text(link_text)
    
@when('the user clicks on the link')
def step_impl(context):
    context.slide_show.clicking_link()

@then('a new page opens up having the URL "{slide_show_page_url}"')           
def step_impl(context, slide_show_page_url):
    context.slide_show.verify_slide_show_pages_url(slide_show_page_url)     
    
@step('there is a slideshow loaded with an image which has the aria-label "{first_aria_label}"')
def step_impl(context, first_aria_label):
    context.slide_show.verify_first_aria_label(first_aria_label)
        
@step('the page has the number one "{page_number}"')
def step_impl(context, page_number):
    context.slide_show.verify_first_slide_page_number(page_number)        
    
@when('the user clicks on the right-arrow on the right of the number 1')
def step_impl(context):
    context.slide_show.click_the_right_arrow()    
    
@then('a new slide-page with another image is loaded')
def step_impl(context):
    context.slide_show.verify_new_slide_page_loaded()

@step('the new image has the aria-label "{second_aria_label}"')    
def step_impl(context, second_aria_label):
    context.slide_show.verify_second_aria_label(second_aria_label)
    
@step('the page has the number "{second_page_number}"')
def step_impl(context, second_page_number):
    context.slide_show.veryify_second_slide_page_number(second_page_number)        
    
@when('the user clicks on the left-arrow on the left of the number 2')
def step_impl(context):
    context.slide_show.click_left_arrow_button()

@then('the first page with the first image is loaded again')
def step_impl(context):
    context.slide_show.verify_first_slide_page_reload()    
    
@step('the first page has the number "{page_number}"')        
def step_impl(context, page_number):
    context.slide_show.verify_first_slide_page_number(page_number)