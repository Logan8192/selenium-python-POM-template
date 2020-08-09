import unittest
import utils.driverUtils as testUtils
from POM.pages.home_page import HomePage
from utils import dataFileUtils


class test_01_search(unittest.TestCase):
    driver = testUtils.start_driver()

    @classmethod
    def setUpClass(cls):
        cls.current_page = None
        cls.data = dataFileUtils.open_datafile("test_01.json")

    def test_step_01_search_criteria(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_page_loaded(), "Home page is not loaded")
        home_page.fill_search_input(self.data["search_criteria"])
        self.assertEqual(home_page.return_search_input_text(), self.data["search_criteria"],
                         "Text contained in the search input was not the expected")
        search_results_page = home_page.click_search_button()
        self.__class__.current_page = search_results_page
        self.assertTrue(search_results_page.is_page_loaded(),
                        "Search Results Page is not loaded after clicking the search button")

    def test_step_02_check_results(self):
        search_results_page = self.current_page
        self.assertEqual(search_results_page.return_search_input_text(), self.data["search_criteria"],
                         "Text contained in the search input was not the expected")
        self.assertEqual(search_results_page.return_selected_tab(), self.data["tabs"]["all"],
                         "'All' tab is not selected by default after clicking the search button in Home page")
        self.assertTrue(search_results_page.are_page_results_displayed(), "There are not page results displayed")

    def test_step_03_check_images_tab(self):
        search_results_page = self.current_page
        search_results_page.click_tab(self.data["tabs"]["images"])
        self.assertEqual(search_results_page.return_selected_tab(), self.data["tabs"]["images"],
                         "'Images' tab is not selected after clicking it")
        self.assertEqual(search_results_page.return_search_input_text(), self.data["search_criteria"],
                         "Text contained in the search input after selecting the 'images' tab was not the expected")
        self.assertTrue(search_results_page.are_image_results_displayed(),
                        "There are not image results displayed after clicking the 'images' tab")

    def test_step_04_check_videos_tab(self):
        search_results_page = self.current_page
        search_results_page.click_tab(self.data["tabs"]["videos"])
        self.assertEqual(search_results_page.return_selected_tab(), self.data["tabs"]["videos"],
                         "'Videos' tab is not selected after clicking it")
        self.assertEqual(search_results_page.return_search_input_text(), self.data["search_criteria"],
                         "Text contained in the search input after selecting the 'videos' tab was not the expected")
        self.assertTrue(search_results_page.are_video_results_displayed(),
                        "There are not image results displayed after clicking the 'videos' tab")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
