from ui_tests.pages.login_page import LoginPage


def test_login_negative_and_positive_pom(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("abc", "abc")
    login_page.expect_error_contains("Your username is invalid!")

    login_page.login("tomsmith", "SuperSecretPassword!")
    login_page.expect_success_contains("You logged into a secure area!")
    login_page.expect_logout_visible()

    login_page.logout()
    login_page.expect_login_screen()
