from pathlib import Path

from ui_tests.pages.upload_page import UploadPage


def test_file_upload_pom(page):
    upload_page = UploadPage(page)

    upload_page.open()
    upload_file = Path(__file__).resolve().parents[2] / "example.txt"
    upload_page.select_file(upload_file)
    upload_page.submit_upload()
    upload_page.expect_uploaded_filename("example.txt")
