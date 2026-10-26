"""
google_search_automation.py

Assignment: Automation using Selenium - Getting Data
Author: Deen Bandhu Singh

What this script demonstrates:
- Creating a WebDriver instance using webdriver.Chrome()
- Opening a web page using driver.get()
- Maximizing the browser window using driver.maximize_window()
- Locating elements using By.NAME and By.XPATH
- Performing a search using send_keys()
- Clicking elements using click()
- Waiting using time.sleep()
- Refreshing the page using driver.refresh()
- Extracting multiple elements using find_elements()
- Printing extracted data to the console using print()
- Closing the browser using driver.quit()
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    search_term = "Selenium WebDriver Python tutorial"

    # 1. Create WebDriver instance
    driver = webdriver.Chrome()

    try:
        # 2. Maximize the browser window
        driver.maximize_window()

        # 3. Open Google
        driver.get("https://www.google.com")
        time.sleep(2)  # wait for the page to load

        # 4. Locate the search box using By.NAME and type the search term
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)  # 5. Submit the search

        time.sleep(2)  # wait for results to load

        # 6. Refresh the results page
        driver.refresh()
        time.sleep(2)

        # 7. Extract multiple elements: all the result headings (h3 tags)
        results = driver.find_elements(By.XPATH, "//h3")

        # 8. Display extracted data in the console
        print(f"Search term: {search_term}")
        print(f"Number of results found on page: {len(results)}\n")
        print("Search result titles:")
        for index, result in enumerate(results, start=1):
            title = result.text.strip()
            if title:
                print(f"{index}. {title}")

        time.sleep(2)

    finally:
        # 9. Close the browser
        driver.quit()


if __name__ == "__main__":
    main()
