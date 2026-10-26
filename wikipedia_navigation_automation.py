"""
wikipedia_navigation_automation.py

Assignment: Automation using Selenium - Getting Data
Author: Deen Bandhu Singh

What this script demonstrates (extra example covering By.LINK_TEXT and
By.CLASS_NAME, which are also required locators for this assignment):
- Creating a WebDriver instance using webdriver.Chrome()
- Opening a web page using driver.get()
- Maximizing the browser window using driver.maximize_window()
- Locating elements using By.NAME, By.LINK_TEXT, and By.CLASS_NAME
- Performing a search using send_keys()
- Clicking a link using By.LINK_TEXT and click()
- Using time.sleep() for wait handling
- Refreshing the page using driver.refresh()
- Extracting multiple elements using find_elements()
- Displaying extracted data in the console using print()
- Closing the browser using driver.quit()
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    search_term = "Selenium (software)"

    # 1. Create WebDriver instance
    driver = webdriver.Chrome()

    try:
        # 2. Maximize the browser window
        driver.maximize_window()

        # 3. Open Wikipedia
        driver.get("https://www.wikipedia.org")
        time.sleep(2)

        # 4. Locate the search box using By.NAME and search
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)

        # 5. Refresh the article page
        driver.refresh()
        time.sleep(2)

        # 6. Locate a link on the article using By.LINK_TEXT and click it
        try:
            contents_link = driver.find_element(By.LINK_TEXT, "History")
            contents_link.click()
            time.sleep(2)
        except Exception:
            print("Note: 'History' link not found on this page, skipping click step.")

        # 7. Extract multiple elements using By.CLASS_NAME (paragraph text)
        paragraphs = driver.find_elements(By.CLASS_NAME, "mw-parser-output")

        # 8. Extract all paragraph <p> tags for readable output
        all_p_tags = driver.find_elements(By.XPATH, "//p")

        # 9. Display extracted data in the console
        print(f"Article searched: {search_term}")
        print(f"Number of paragraph blocks found: {len(all_p_tags)}\n")
        print("First few paragraphs of the article:")
        count = 0
        for p in all_p_tags:
            text = p.text.strip()
            if text:
                count += 1
                print(f"\nParagraph {count}:\n{text[:300]}...")
            if count >= 3:
                break

        time.sleep(2)

    finally:
        # 10. Close the browser
        driver.quit()


if __name__ == "__main__":
    main()
