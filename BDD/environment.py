from pages.login_page import LoginPage
from pages.search_page import SearchPage
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.login_page_object = LoginPage()
    context.search_page_object = SearchPage()

def after_all(context):
    context.browser.close()