from playwright.sync_api import expect

from ui_tests.pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

    def open(self) -> None:
        self.page.goto(self.URL)

    def start_loading(self) -> None:
        self.page.get_by_role("button", name="Start").click()

    def expect_hello_world(self, timeout: int = 15000) -> None:
        finish = self.page.locator("#finish")
        expect(finish).to_be_visible(timeout=timeout)
        expect(finish).to_have_text("Hello World!", timeout=timeout)
