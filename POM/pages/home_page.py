from selenium.webdriver.common.by import By
from ..base_page import BasePage
from ..pages.search_results_page import SearchResultsPage


class HomePageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search_form_input_homepage")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search_button_homepage")


class HomePage(BasePage):

    def is_page_loaded(self):
        """
        Checks if the Home page is loaded by trying to find the search input element.
        :return: True if the page is loaded.
        :rtype: bool
        """
        return self.is_element_present(HomePageLocators.SEARCH_INPUT)

    def fill_search_input(self, criteria):
        """
        Fills the search input.
        :param criteria: (string) Text to search.
        """
        self.fill_in(HomePageLocators.SEARCH_INPUT, criteria)

    def click_search_button(self):
        """
        Clicks the search button.
        :return: SearchResultsPage POM instance.
        """
        self.click(HomePageLocators.SEARCH_BUTTON)
        return SearchResultsPage(self.driver)

    def return_search_input_text(self):
        """
        Returns the text contained in the search input.
        :return: Text contained in the search input.
        :rtype: string
        """
        return self.return_text_in_input(HomePageLocators.SEARCH_INPUT)
