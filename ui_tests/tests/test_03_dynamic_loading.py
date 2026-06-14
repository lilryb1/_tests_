from playwright.sync_api import expect


def test_dynamic_loading_without_sleep(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

    page.get_by_role("button", name="Start").click()

    finish = page.locator("#finish")
    expect(finish).to_be_visible(timeout=15000)
    expect(finish).to_have_text("Hello World!", timeout=15000)
