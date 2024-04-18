from features.Pages.base_page import BasePage
from features.Pages.library_page import Library
from time import sleep

class EditButton(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.libs = Library()