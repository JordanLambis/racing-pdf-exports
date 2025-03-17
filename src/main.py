import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils import set_up_chrome_driver_for_site, wait_and_obtain_element

horse_url = "https://tab.co.za/tabs/external;link=https:%2F%2Fcontent.4racing.com%2Fracecards%3Fnoglobalcontent%3Dtrue"

# Set up the driver
driver = set_up_chrome_driver_for_site(url=horse_url)

# Wait for the elements to be available
try:
    time.sleep(10)
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="inner-container"]')))

    # Print the number of elements found
    print(f"Found {len(elements)} elements")

    # Optional: Print text of elements
    for element in elements:
        print(element.text)

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()  # Close the driver properly
