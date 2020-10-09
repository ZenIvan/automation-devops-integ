from zenrooms_tests.page_actions import PageActions

class Login(PageActions):

    def test_login_successfully(self):
        self.login_backoffice()
        self.is_text_visible("qa_automation admin", "#main-navbar-collapse > div > ul > li > a > span")
