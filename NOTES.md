SeleniumAutomation-DeenBandhuSingh
==================================

Assignment: Automation using Selenium - Getting Data
Author: Deen Bandhu Singh

Contents
--------
1. google_search_automation.py
   - Opens Google, searches a term, refreshes the page, and extracts/prints
     search result titles.
   - Locators used: By.NAME, By.XPATH

2. amazon_search_automation.py
   - Opens Amazon, searches for a product, clicks the search button,
     refreshes the page, and extracts/prints product titles and prices.
   - Locators used: By.ID, By.XPATH, By.CLASS_NAME

3. wikipedia_navigation_automation.py
   - Opens Wikipedia, searches an article, clicks a link on the page using
     link text, refreshes, and extracts/prints paragraph text.
   - Locators used: By.NAME, By.LINK_TEXT, By.CLASS_NAME, By.XPATH

Together, the three scripts cover every requirement in the assignment:
webdriver.Chrome(), driver.get(), driver.maximize_window(),
By.NAME / By.CLASS_NAME / By.LINK_TEXT / By.XPATH, send_keys(), click(),
time.sleep(), driver.refresh(), find_elements(), print(), and driver.quit().

How to run
----------
1. Install Python 3.8 or later.

2. Install the required package:
       pip install -r requirements.txt

3. Make sure Google Chrome is installed on your machine.
   Selenium 4.10+ automatically downloads and manages the matching
   ChromeDriver, so no separate driver download is normally required.
   (If it is not automatic on your Selenium version, download the
   ChromeDriver that matches your Chrome version from
   https://chromedriver.chromium.org/downloads and place it on your PATH.)

4. Run any script from a terminal, for example:
       python google_search_automation.py
       python amazon_search_automation.py
       python wikipedia_navigation_automation.py

5. Each script will:
   - Open a Chrome browser window
   - Perform the automated search/navigation
   - Refresh the page where required
   - Print the extracted data to the terminal
   - Close the browser automatically at the end

Notes
-----
- Websites like Google and Amazon frequently change their page structure
  (element IDs/classes), and may show CAPTCHAs or consent pop-ups for
  automated browsers. If a locator fails, inspect the page (right-click ->
  Inspect) and update the corresponding By.* locator in the script.
- These scripts include time.sleep() calls for simple wait handling as
  required by the assignment; for production-grade code,
  WebDriverWait with expected_conditions would normally be preferred.
