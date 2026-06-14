from playwright.sync_api import expect


def test_add_remove_elements(page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    add_button = page.get_by_role("button", name="Add Element")
    for _ in range(3):
        add_button.click()

    delete_buttons = page.get_by_role("button", name="Delete")
    expect(delete_buttons).to_have_count(3)

    delete_buttons.first.click()
    expect(delete_buttons).to_have_count(2)

    while delete_buttons.count() > 0:
        delete_buttons.first.click()

    expect(delete_buttons).to_have_count(0)
