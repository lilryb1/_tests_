from pathlib import Path

from playwright.sync_api import expect


def test_file_upload(page):
    page.goto("https://the-internet.herokuapp.com/upload")

    upload_file = Path(__file__).resolve().parents[2] / "example.txt"
    page.locator("#file-upload").set_input_files(upload_file)
    page.get_by_role("button", name="Upload").click()

    expect(page.locator("#uploaded-files")).to_have_text("example.txt")
