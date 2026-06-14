from playwright.sync_api import expect

from ui_tests.pages.base_page import BasePage


class AlertsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def open(self) -> None:
        self.page.goto(self.URL)

    def accept_js_alert(self) -> None:
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("button", name="Click for JS Alert").click()

    def dismiss_js_confirm(self) -> None:
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.page.get_by_role("button", name="Click for JS Confirm").click()

    def accept_js_prompt(self, text: str) -> None:
        self.page.once("dialog", lambda dialog: dialog.accept(text))
        self.page.get_by_role("button", name="Click for JS Prompt").click()

    def expect_result(self, text: str) -> None:
        expect(self.page.locator("#result")).to_have_text(text)
