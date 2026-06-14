from playwright.sync_api import expect

from ui_tests.pages.base_page import BasePage


class AddRemoveElementsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def open(self) -> None:
        self.page.goto(self.URL)

    def add_elements(self, count: int) -> None:
        add_button = self.page.get_by_role("button", name="Add Element")
        for _ in range(count):
            add_button.click()

    def remove_one_element(self) -> None:
        self.page.get_by_role("button", name="Delete").first.click()

    def remove_all_elements(self) -> None:
        delete_buttons = self.page.get_by_role("button", name="Delete")
        while delete_buttons.count() > 0:
            delete_buttons.first.click()

    def expect_delete_count(self, count: int) -> None:
        expect(self.page.get_by_role("button", name="Delete")).to_have_count(count)
