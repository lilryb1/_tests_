from ui_tests.pages.dynamic_loading_page import DynamicLoadingPage


def test_dynamic_loading_without_sleep_pom(page):
    dynamic_page = DynamicLoadingPage(page)

    dynamic_page.open()
    dynamic_page.start_loading()
    dynamic_page.expect_hello_world(timeout=15000)
