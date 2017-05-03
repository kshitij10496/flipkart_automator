# flipkart_automator
Using Selenium and Page Object pattern, I have written a script which extracts the most popular laptops on Flipkart.

## Execution

1. Download/Clone this repository :    `git clone https://github.com/kshitij10496/flipkart_automator.git`
    
2. Install the Chrome Driver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

3. Install Selenium Python bindings :   `pip install selenium`

Supported Python versions : 2.7+ and 3.5+

     python flipscript.py

Python Unittest framework is used for writing the unit tests for browser automation.  
In order to run the tests,

    python test_flipscript.py

## File Structure

     -- flipscript.py  - main script
    |
     -- test_flipscript.py - automation test script
    |
     -- pageobjects
        |
         -- __init__.py
        |
         -- errors.py - user-defined exceptions
        |
         -- laptops.py - models the Laptop product
        |
         -- page.py - abstracts the Flipkart webpage
        |
         -- textelement.py - text element
        |
         -- webdriver.py - minimalistic wrapper around the Selenium Chrome Driver
        |
         -- webelement.py - abstracts an element of DOM
