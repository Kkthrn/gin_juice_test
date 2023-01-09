from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 0.3)

    def get_by(self, find_by: str):
        find_by = find_by.lower()
        locating = {'name': By.NAME,
                    'xpath': By.XPATH,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'tag_name': By.TAG_NAME,
                    'part_link_text': By.PARTIAL_LINK_TEXT,
                    'class_name': By.CLASS_NAME,
                    'css': By.CSS_SELECTOR}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None):
        return self.wait.until(ec.visibility_of_element_located((self.get_by(find_by), locator)), locator_name)