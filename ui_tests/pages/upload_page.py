from pathlib import Path

from playwright.sync_api import expect

from ui_tests.pages.base_page import BasePage


class UploadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/upload"

    def open(self) -> None:
        self.page.goto(self.URL)

    def select_file(self, file_path: Path) -> None:
        self.page.locator("#file-upload").set_input_files(file_path)

    def submit_upload(self) -> None:
        self.page.get_by_role("button", name="Upload").click()

    def expect_uploaded_filename(self, filename: str) -> None:
        expect(self.page.locator("#uploaded-files")).to_have_text(filename)
