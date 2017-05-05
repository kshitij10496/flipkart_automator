import time
from .textelement import Text
from .errors import ExpectedElementError, WaitForElementError
from .laptop import Laptop

class BasePage(object):
    timeout_seconds = 20
    sleep_interval = .25

    def __init__(self, driver):
        self.driver = driver

    @property
    def referrer(self):
        return self.driver.execute_script('return document.referrer')

    def sleep(self, seconds=None):
        if seconds:
            time.sleep(seconds)
        else:
            time.sleep(self.sleep_interval)

    def find_element_by_locator(self, locator):
        return self.driver.find_element_by_locator(locator)

    def find_elements_by_locator(self, locator):
        return self.driver.find_elements_by_locator(locator)

    def wait_for_available(self, locator):
        for i in range(self.timeout_seconds):
            if self.driver.is_element_available(locator):
                break
            self.sleep()
        else:
            raise WaitForElementError('Wait for available timed out')
        return True

    def wait_for_visible(self, locator):
        for i in range(self.timeout_seconds):
            if self.driver.is_visible(locator):
                break
            self.sleep()
        else:
            raise WaitForElementError('Wait for visible timed out')
        return True

    def wait_for_hidden(self, locator):
        for i in range(self.timeout_seconds):

            if self.driver.is_visible(locator):
                self.sleep()
            else:
                break
        else:
            raise WaitForElementError('Wait for hidden timed out')
        return True

    def wait_for_alert(self):
        for i in range(self.timeout_seconds):
            try:
                alert = self.driver.switch_to_alert()
                if alert.text:
                    break
            except NoAlertPresentException as nape:
                pass
            self.sleep()
        else:
            raise NoAlertPresentException(msg='Wait for alert timed out')
        return True

page_url = 'http://flipkart.com'

locators = {
    'search_field': ('name', 'q'),
    'suggestions': ('class', 'col-11-12'),
    'sorting_options': ('class', '_1No1qI'),
    'popularity': ('xpath', "//li[text()='Popularity']"),
    'product_details': ('class', '_1-2Iqu'),
    'footer': ('class', 'HJlsB9'),
    'submit_button': ('class', 'vh79eN'),
    'no_results': ('class', '_1GL7J5')
}

class SearchTextElement(Text):
    locator = locators['search_field']


class FlipkartWelcomePage(BasePage):
    search_text = SearchTextElement()
    
    def open(self):
        self.driver.get(page_url)
        return self.wait_until_loaded()

    def wait_until_loaded(self):
        self.driver.is_element_available(locators['footer'])
        return self

    @property
    def has_search(self):
        return self.driver.is_element_available(locators['search_field'])

    @property
    def has_suggestions(self):
        return self.driver.is_element_available(locators['suggestions'])

    @property
    def has_submit(self):
        return self.driver.is_element_available(locators['submit_button'])

    def title_contains(self, text):
        return text in self.driver.title

    def click_submit(self):
        if self.has_submit:
            submit_button = self.find_element_by_locator(locators['submit_button'])
            submit_button.click()
            return FlipkartSearchPage(self.driver).wait_until_loaded()
        else:
            raise ExpectedElementError('No Submit button available.')

class FlipkartSearchPage(BasePage):

    def wait_until_loaded(self):
        self.wait_for_available(locators['product_details'])
        return self

    @property
    def has_results(self):
        return not self.driver.is_visible(locators['no_results'])

    @property
    def has_sorting_options(self):
        return self.driver.is_element_available(locators['sorting_options'])

    def sort_by(self, predicate=None):
        '''Sorts the results by popularity.

        predicate: String, optional
            Can be either of 'popularity'
        '''
        if self.has_sorting_options:
           sorting_popularity = self.find_element_by_locator(locators[predicate])
           sorting_popularity.click()
           return FlipkartSearchPage(self.driver).wait_until_loaded()
        else:
            raise ExpectedElementError('No sorting options available.')

    def get_details(self):
        results = self.find_element_by_locator(('class', '_1ZODb3')).text
        self.total_results = results.split()[-4]

        pages = self.find_element_by_locator(('class', '_3v8VuN')).text
        self.total_pages = pages.split()[-1]

    def get_results(self, max_items=5):
        '''Scrapes the products from the first page of the search result.'''
        if self.has_results:
            products = self.find_elements_by_locator(locators['product_details'])[:max_items]
            laptops = [Laptop(p.text) for p in products] # since the search item is laptop
            return laptops
        else:
            return None
