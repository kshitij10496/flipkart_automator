import unittest
from pageobjects.webdriver import WebDriver
from pageobjects.page import FlipkartWelcomePage, FlipkartSearchPage

class FlipkartLaptopSearch(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriver()
        
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_search(self):
        # Load the Flipkart site
        welcome_page = FlipkartWelcomePage(self.driver).open()
        
        # Test 01: Check whether the correct site is loaded or not
        self.assertTrue(welcome_page.title_contains('Flipkart'))
        # TODO: display a suitable message for assertion failure

        # Test 02: Check if the page contains a Search Box
        self.assertTrue(welcome_page.has_search)

        # Perform search for "laptop"
        welcome_page.search_text = 'laptop'
        
        # Test 03: Check whether the suggestions box is displayed or not
        self.assertTrue(welcome_page.has_suggestions)
        
        # Test 04: Check whether the page has a submit button
        self.assertTrue(welcome_page.has_submit)

        # Click the submit button
        results_page = welcome_page.click_submit()

        # Test 05: Check if results exists on the page or not.
        self.assertTrue(results_page.has_results)

        # Test 06: Check if the results on the page can be sorted through "Popularity"
        self.assertTrue(results_page.has_sorting_options)
        
        # Sorts by Popularity
        sorted_results_page = results_page.sort_by('popularity')

        # Test 07: Checks if results exists on the page or not.
        self.assertTrue(sorted_results_page.has_results)

if __name__ == '__main__':
    unittest.main()
