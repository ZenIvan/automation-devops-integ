from seleniumbase import BaseCase

class PageObject(BaseCase):
    html = "html"



class PageActions(PageObject):

    def visit_zenrooms_home_page(self, url):
        self.open(url)       

    def visit_zenrooms_backoffice(self, url):
        self.open(url)    
    
    def visit_hotelier_website(self, url):
        self.open(url)

    def login_backoffice(self):
        self.type("#email","qa_automation_admin@zenrooms.com")
        self.type("#password", "admin")
        self.click("#login-group > input")

    def login_hotelier(self):
        self.type("#email","qa_automation_admin@zenrooms.com")
        self.type("#password", "admin")
        self.click("#login-group > input")

    def logout_backoffice(self):
        self.click() # logged in name
        self.click() # dropdown logout button

class ZenroomsUI(PageActions):

    def test_zenrooms_home_page(self):
        '''
        1. Visit homepage
        2. Assert that page is loaded
        3. Login
        4. Assert that user is logged in
        5. Logout
        6. Assert that user is logged out successfully
        '''
        self.visit_zenrooms_home_page()
        self.is_element_visible("#currency_switch")
        self.is_element_visible("language_switch")
        self.is_element_visible("#searchText")

    def test_login_backoffice_successfully(self):
        '''
        1. Login backoffice
        2. Assert that user is logged in
        3. Logout
        4. Assert that user is logged out successfully
        '''
        self.login_backoffice()
        self.is_text_visible("qa_automation admin", "#main-navbar-collapse > div > ul > li > a > span")
        self.logout_backoffice()
        self.assert_user_is_logged_out()

    def test_login_hotelier_website_successfully(self):
        '''
        1. Login hotelier website
        2. Assert that user is logged in
        3. Logout
        4. Assert that user is logged out successfully
        '''
        self.login_hotelier()
        self.is_text_visible("qa_automation admin", "#main-navbar-collapse > div > ul > li > a > span")
        self.logout_hotelier()
        self.assert_user_is_logged_out()

    def test_view_deals_page(self):
        '''
        Pre-condition: Deals page must be setup in backoffice > content page
        1. Login backoffice
        2. Assert that user is logged in
        3. Logout
        4. Assert that user is logged out successfully
        '''
        self.open()
        self.assert_page_is_loaded()