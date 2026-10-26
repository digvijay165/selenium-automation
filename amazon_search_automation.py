"""
amazon_search_automation.py

Assignment: Automation using Selenium - Getting Data
Author: Deen Bandhu Singh

What this script demonstrates:
- Creating a WebDriver instance using webdriver.Chrome()
- Opening a web page (Amazon) using driver.get()
- Maximizing the browser window using driver.maximize_window()
- Locating elements using By.ID, By.CLASS_NAME, and By.XPATH
- Performing a search operation using send_keys()
- Clicking elements using click()
- Using time.sleep() for wait handling
- Refreshing the page using driver.refresh()
- Extracting multiple elements using find_elements()
- Displaying extracted data in the console using print()
- Closing the browser using driver.quit()
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    product_to_search = "laptop"

    # 1. Create WebDriver instance
    driver = webdriver.Chrome()

    try:
        # 2. Maximize the browser window
        driver.maximize_window()

        # 3. Open Amazon
        driver.get("https://www.amazon.in")
        time.sleep(3)  # wait for the page to fully load

        # 4. Locate the search box using By.ID and type the product name
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(product_to_search)

        # 5. Locate and click the search button using By.ID
        search_button = driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()

        time.sleep(3)  # wait for search results to load

        # 6. Refresh the search results page
        driver.refresh()
        time.sleep(3)

        # 7. Extract multiple elements: product titles using By.CLASS_NAME / By.XPATH
        product_titles = driver.find_elements(
            By.XPATH, "//div[@data-component-type='s-search-result']//h2//span"
        )

        # 8. Extract multiple elements: product prices using By.CLASS_NAME
        product_prices = driver.find_elements(By.CLASS_NAME, "a-price-whole")

        # 9. Display extracted data in the console
        print(f"Searched product: {product_to_search}")
        print(f"Number of product titles found: {len(product_titles)}\n")

        print("Product titles:")
        for index, title in enumerate(product_titles[:10], start=1):
            text = title.text.strip()
            if text:
                print(f"{index}. {text}")

        print("\nProduct prices (partial list):")
        for index, price in enumerate(product_prices[:10], start=1):
            text = price.text.strip()
            if text:
                print(f"{index}. Rs. {text}")

        time.sleep(2)

    finally:
        # 10. Close the browser
        driver.quit()


if __name__ == "__main__":
    main()
