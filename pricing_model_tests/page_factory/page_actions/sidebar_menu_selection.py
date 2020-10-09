from pricing_model_tests.page_factory.page_actions.utility_class import UtilityClass


class SidebarAction(UtilityClass):
    # Selects an item on the sidebar to navigate to a specific page
    def select_sidebar_item(self, item):
        self.click(f'//div[@class="sidebar-sticky"]/ul[1]/li/a[contains(., "{item}")]')
