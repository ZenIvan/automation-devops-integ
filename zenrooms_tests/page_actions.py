from seleniumbase import BaseCase

class PageActions(BaseCase):

    def visit_zenrooms_home_page(self, url="https://www-staging.zenrooms.com/"):
        self.open(url)       

    def login_backoffice(self, url="https://ops-staging.zenrooms.com/"):
        self.open(url)
        self.type("#email","qa_automation_admin@zenrooms.com")
        self.type("#password", "admin")
        self.click("#login-group > input")