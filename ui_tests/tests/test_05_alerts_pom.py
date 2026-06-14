from ui_tests.pages.alerts_page import AlertsPage


def test_js_alert_confirm_and_prompt_pom(page):
    alerts_page = AlertsPage(page)

    alerts_page.open()

    alerts_page.accept_js_alert()
    alerts_page.expect_result("You successfully clicked an alert")

    alerts_page.dismiss_js_confirm()
    alerts_page.expect_result("You clicked: Cancel")

    alerts_page.accept_js_prompt("Tekst z prompta")
    alerts_page.expect_result("You entered: Tekst z prompta")
