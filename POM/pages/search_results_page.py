from selenium.webdriver.common.by import By
from ..page import Page


class SearchResultsPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search_form_input")
    SELECTED_TAB = (By.CSS_SELECTOR, ".zcm__item .is-active")
    PAGE_RESULTS = (By.CSS_SELECTOR, ".result__body")
    IMAGE_RESULTS = (By.CSS_SELECTOR, ".tile--img__media")
    VIDEO_RESULTS = (By.CSS_SELECTOR, ".tile--vid")
    TAB = "//li[@class='zcm__item']/a[text()='{}']"


class SearchResultsPage(Page):

    def are_page_results_displayed(self):
        """
        Checks if the results are displayed in the 'all' tab.
        :return: True if the search displayed results.
        :rtype: bool
        """
        return self.is_element_present(SearchResultsPageLocators.PAGE_RESULTS)

    def are_image_results_displayed(self):
        """
        Checks if image results are displayed in the 'images' tab.
        :return: True if the search displayed results.
        :rtype: bool
        """
        return self.is_element_present(SearchResultsPageLocators.IMAGE_RESULTS)

    def are_video_results_displayed(self):
        """
        Checks if video results are displayed in the 'videos' tab.
        :return: True if the search displayed results.
        :rtype: bool
        """
        return self.is_element_present(SearchResultsPageLocators.VIDEO_RESULTS)

    def click_tab(self, tab_name):
        """
        Clicks a tab by its name.
        :param tab_name: Name of the tab.
        """
        self.click((By.XPATH, SearchResultsPageLocators.TAB.format(tab_name)))

    def is_page_loaded(self):
        """
        Checks if the Home page is loaded by trying to find the search input element.
        :return: True if the page is loaded.
        """
        return self.is_element_present(SearchResultsPageLocators.SEARCH_INPUT)

    def return_search_input_text(self):
        """
        Returns the text contained in the search input.
        :return: Text contained in the search input.
        :rtype: string
        """
        return self.return_text_in_input(SearchResultsPageLocators.SEARCH_INPUT)

    def return_selected_tab(self):
        """
        Returns the name of the selected tab.
        :return: Name of the selected tab.
        :rtype: string
        """
        return self.return_element_text(SearchResultsPageLocators.SELECTED_TAB)
