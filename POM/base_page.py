from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=10):
        """
        Clicks a given web element.
        :param locator: Locator of the element to click.
        :param timeout: (int) Seconds to wait for the element.
        """
        self.find_element(locator, timeout).click()

    def fill_in(self, locator, criteria, timeout=10):
        """
        Fills a given input text.
        :param locator: Locator of the element to fill.
        :param criteria: Word to fill in the input.
        :param timeout: (int) Seconds to wait for the element.
        """
        element = self.find_element(locator, timeout)
        element.send_keys(criteria)

    def find_element(self, locator, timeout=10):
        """
        Finds a element by a given locator.
        :param locator: Locator of the element to find.
        :param timeout: (int) Seconds to wait for the element.
        :return: Web element found.
        :rtype: webelement
        """
        self.wait_for_element(locator, timeout)
        return self.driver.find_element(*locator)

    def find_elements(self, locator, timeout=10):
        """
        Finds a group of element by a given locator.
        :param locator: Locator of the elements to find.
        :param timeout: (int) Seconds to wait for the elements.
        :return: Web elements found.
        :rtype: list
        """
        self.wait_for_element(locator, timeout)
        return self.driver.find_elements(*locator)

    def is_element_present(self, locator, timeout=10):
        """
        Checks if a given element is present in the page.
        :param locator: Locator of the element.
        :param timeout: (int) Seconds to wait for the element.
        :return: True if the element is present.
        :rtype: bool
        """
        element = self.find_element(locator, timeout)
        return True if element else False

    def move_to_element(self, locator, timeout=10):
        """
        Moves to an element.
        :param locator: Locator of the element.
        :param timeout: (int) Seconds to wait for the element.
        """
        element = self.find_element(locator, timeout)
        ActionChains(self.driver).move_to_element(element).perform()

    def return_text_in_input(self, locator, timeout=10):
        """
        Returns the text contained in a given input element.
        :param locator: Locator of the element.
        :param timeout: (int) Seconds to wait for the element.
        :return: Text contained in the input.
        :rtype: string
        """
        return self.find_element(locator, timeout).get_attribute("value")

    def return_element_text(self, locator):
        """
        Returns the text contained in a given element
        :param locator: Locator of the element.
        :return: Text contained in the element.
        :rtype: string
        """
        return self.find_element(locator).text

    def wait_for_element(self, locator, timeout=10):
        """
        Waits for a given element for a given time in seconds.
        :param locator: Locator of the element.
        :param timeout: (int) Seconds to wait for the element.
        """
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator),
            message=f"Unable to locate the element: {locator} after {timeout} seconds.")
