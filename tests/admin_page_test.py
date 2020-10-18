from pages.AdminPage import AdminPage


def test_login(browser):
    admin_page = AdminPage(browser)
    admin_page.go_to_site()
    admin_page.login('admin', 'admin')
    title = browser.title
    assert 'My Store' in title
