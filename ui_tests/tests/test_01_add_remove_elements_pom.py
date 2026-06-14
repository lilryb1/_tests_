from ui_tests.pages.add_remove_elements_page import AddRemoveElementsPage


def test_add_remove_elements_pom(page):
    add_remove_page = AddRemoveElementsPage(page)

    add_remove_page.open()
    add_remove_page.add_elements(3)
    add_remove_page.expect_delete_count(3)

    add_remove_page.remove_one_element()
    add_remove_page.expect_delete_count(2)

    add_remove_page.remove_all_elements()
    add_remove_page.expect_delete_count(0)
