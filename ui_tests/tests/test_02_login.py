from playwright.sync_api import expect


def test_login_negative_and_positive(page):
    page.goto("https://the-internet.herokuapp.com/login")

    username = page.get_by_label("username")
    password = page.get_by_label("password")
    login = page.get_by_role("button", name="Login")

    username.fill("abc")
    password.fill("abc")
    login.click()

    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")

    username.fill("tomsmith")
    password.fill("SuperSecretPassword!")
    login.click()

    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    expect(page.get_by_role("link", name="Logout")).to_be_visible()

    page.get_by_role("link", name="Logout").click()

    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.get_by_role("link", name="Logout")).to_have_count(0)
