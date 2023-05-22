from pages.web_elements import *
from pages.web_page import WebPage
import allure

class MainPage(WebPage):

    #def account_button(self, username) -> WebElement: return el(self.page, selector='a[href="#@%s"]' % username)
    #def loader(self) -> WebElement: return el(self.page, "text='Loading...'")
    #def settings_link(self) -> WebElement: return el(self.page, selector='a[href="#settings"]')
    #def editor_link(self) -> WebElement: return el(self.page, selector='a[href="#editor"]')
    def login_button(self)-> WebElement: return el(self.page, selector='a[href="#login"]')
    #def register_button(self)-> WebElement: return el(self.page, element=s(self.page, 'text="Sign up"'))
    #def articles(self)-> WebElementsCollection: return elc(self.page, elements=ss(self.page, ".article-preview"), element_container=Article)
    #def nav_bar(self): return NavBar(self.page, "nav[class*='navbar']")

    def __init__(self, base_url, page: Page):
        super().__init__(page)
        self.base_url = base_url

    # Open Main Page
    @allure.step
    def open(self):
        self.page.goto("%s/#/" % self.base_url, wait_until="load")
        return self

    @allure.step("Press SignIn button")
    def login(self):
        self.login_button().click()
        from pages.login_page.login_page import LoginPage
        return LoginPage(self.base_url, self.page)
