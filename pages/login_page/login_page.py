from pages.web_elements import *
from pages.web_page import WebPage
from pages.main_page.main_page import MainPage
from models.user import User
import allure


class LoginPage(WebPage):

    # Define wrapped Playwright Elements
    def id_field(self)-> WebElement: return el(self.page, selector='input[type="text"]')
    def password_field(self)-> WebElement: return el(self.page, selector='input[type="password"]')
    def submit_button(self)-> WebElement: return el(self.page, selector='button[type="submit"]')
    def error_message(self)-> WebElement: return el(self.page, selector='.error-messages > li')

    def __init__(self, base_url, page: Page):
        super().__init__(page)
        self.base_url = base_url
        self.s = lambda css: self.page.query_selector(css)

    # Open Login Page
    @allure.step
    def open(self):
        self.page.goto(self.base_url)
        return self

    # Authorize
    @allure.step('Login user with id: "{id}", password: "{password}"')
    def login(self, id, password):
        self.id_field().val(id).press_tab()
        self.password_field().val(password).press_enter()
        return MainPage(self.base_url, self.page)

    @allure.step('Login with user: "{1}"')
    def login_with(self, user: User):
        self.id_field().val(user.id).press_tab()
        self.password_field().val(user.password)
        self.submit_button().click()
        return MainPage(self.base_url, self.page)

    # def login(self, email, password):
    #     elf.s(css='input[type="email"]').fill(email)
    #     self.s(css='input[type="password"]').fill(password)
    #     self.s(css='button[type="submit"]').click()