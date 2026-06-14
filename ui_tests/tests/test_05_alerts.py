from playwright.sync_api import expect


def test_js_alert_confirm_and_prompt(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Alert").click()
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")

    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Click for JS Confirm").click()
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")

    page.once("dialog", lambda dialog: dialog.accept("Tekst z prompta"))
    page.get_by_role("button", name="Click for JS Prompt").click()
    expect(page.locator("#result")).to_have_text("You entered: Tekst z prompta")
