from methods.BaseApp import BasePage


def test_check_browser_open(browser):
    base_page = BasePage(browser)
    base_page.go_to_site()
