from playwright.sync_api import expect

from ui_tests.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    def open(self) -> None:
        self.page.goto(self.URL)

    def login(self, username: str, password: str) -> None:
        self.page.get_by_label("username").fill(username)
        self.page.get_by_label("password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def logout(self) -> None:
        self.page.get_by_role("link", name="Logout").click()

    def expect_error_contains(self, text: str) -> None:
        expect(self.page.locator("#flash")).to_contain_text(text)

    def expect_success_contains(self, text: str) -> None:
        expect(self.page.locator("#flash")).to_contain_text(text)

    def expect_logout_visible(self) -> None:
        expect(self.page.get_by_role("link", name="Logout")).to_be_visible()

    def expect_login_screen(self) -> None:
        expect(self.page.get_by_role("button", name="Login")).to_be_visible()
        expect(self.page.get_by_role("link", name="Logout")).to_have_count(0)
