from pathlib import Path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver


DATA_FOLDER = Path(__file__).parent.parent / "data"
CHROME_DRIVER_PATH = Path(__file__).parent.parent / "chromedriver"


def set_up_chrome_driver_for_site(url: str, cookie_element_xpath: str | None = None, by_type = By.XPATH, headless_window = False) -> WebDriver:
    options = Options()
    if headless_window:
        options.add_argument("--headless")
    service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    if cookie_element_xpath:
        try:
            cookie_clear_element = wait_and_obtain_element(driver, by_type, cookie_element_xpath)
            cookie_clear_element.send_keys(Keys.ENTER)
        except Exception as e:
            print(e)

    return driver


def wait_and_obtain_element(driver: WebDriver, element_type: By, element_identifier: str, timeout_seconds=5) -> WebElement:
    WebDriverWait(driver, timeout_seconds).until(
        expected_conditions.presence_of_element_located((element_type, element_identifier))
    )
    return driver.find_element(element_type, element_identifier)