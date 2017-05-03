from pageobjects.webdriver import WebDriver
from pageobjects.page import FlipkartWelcomePage, FlipkartSearchPage

def main():
    # Initiates the Chrome Browser
    chrome_driver = WebDriver()

    # Load the Flipkart site
    welcome_page = FlipkartWelcomePage(chrome_driver).open()
    
    # Perform search for "laptop"
    welcome_page.search_text = 'laptop'
    results_page = welcome_page.click_submit()

    # Sorts by Popularity
    sorted_results_page = results_page.sort_by('popularity')
    
    # Extract some details from the search
    sorted_results_page.get_details()
    number_of_results = sorted_results_page.total_results
    number_of_pages = sorted_results_page.total_pages
    print('The total number of laptops = {}'.format(number_of_results))
    print('The total number of pages = {}'.format(number_of_pages))
    print('=========================\n\n')

    # Print the details of 5 most popular laptops
    laptops = sorted_results_page.get_results(max_items=5)
    for laptop in laptops:
        print(laptop)
        print('------------------\n\n')

    # Close and Quit the driver
    chrome_driver.close()
    chrome_driver.quit()

if __name__ == '__main__':
    main()