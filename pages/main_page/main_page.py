from pages.web_elements import *
from pages.web_page import WebPage
import allure

class MainPage(WebPage):

    def account_button(self, username) -> WebElement: return el(self.page, selector='a[href="https://nid.naver.com/user2/api/route.nhn?m=routePcProfileModification"]')
    #def loader(self) -> WebElement: return el(self.page, "text='Loading...'")
    #def settings_link(self) -> WebElement: return el(self.page, selector='a[href="#settings"]')
    #def editor_link(self) -> WebElement: return el(self.page, selector='a[href="#editor"]')
    def login_button(self)-> WebElement: return el(self.page, selector='a[href="https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"]')
    def register_button(self)-> WebElement: return el(self.page, element=s(self.page, 'text="회원가입"'))
    #def articles(self)-> WebElementsCollection: return elc(self.page, elements=ss(self.page, ".article-preview"), element_container=Article)
    #def nav_bar(self): return NavBar(self.page, "nav[class*='navbar']")
    def user_info(self) -> WebElement: return el(self.page, selector='span[class="MyView-module__nickname___fcxwI"]')

    def __init__(self, base_url,  page: Page):
        super().__init__(page)
        self.base_url = base_url

    # Open Main Page
    @allure.step
    def open(self):
        self.page.goto(self.base_url, wait_until="load")
        return self

    @allure.step("Press SignIn button")
    def login(self):
        self.login_button().click()
        from pages.login_page.login_page import LoginPage
        return LoginPage(self.base_url, self.page)
