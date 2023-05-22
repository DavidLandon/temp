from pages.web_elements import *
from pages.web_elements import Page
from pages.web_page import WebPage
from models.user import User
import allure

class LoginPage(WebPage):
    def email_field(self) -> WebElement: return el(self.page, selector='input[type="text"]')
    def password_field(self) -> WebElement: return el(self.page, selector='input[type="password"]')
    def login_button(self) -> WebElement: return el(self.page, selector='button[type="password"]')

    def __init__(self, base_url, page: Page):
        super().__init__(page)
        self.base_url = base_url
        self.s = lambda css: self.page.query_selector(css)