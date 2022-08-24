from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class CommonPage:

    def __init__(self, driver):
        self.driver = driver
    
    def _go_to(self, url):
        """
        Go to a specific URL
        Args:
            url (str): the url to go, e.g https://example.com
        """
        self.driver.get(url)

    def _element_is_visible(self, locator):
        """
        Verify the element identified by locator is visible. This method attempts to scroll the element
        into view if it is not visible
        Args:
            locator (dict): the element's strategy to be located and the locator value
            e.g {"by": By.XPATH, "value": "//li[@class]"}
        Returns:
            (bool): whether the element is visible or not
        """
        try:
            self._scroll_to_element(locator)
            return self._find_element(locator).is_displayed()
        except NoSuchElementException:
            return False
    
    def _find_element(self, locator):
        """
        Find a web element identified by locator
        Args:
            locator (dict): the element's strategy to be located and the locator value
            e.g {"by": By.XPATH, "value": "//li[@class]"}
        Returns:
            (WebElement): the web element found
        """
        return self.driver.find_element(locator["by"], locator["value"])
    
    def _find_elements(self, locator):
        """
        Find web elements identified by locator
        Args:
            locator (dict): the element's strategy to be located and the locator value
            e.g {"by": By.XPATH, "value": "//li[@class]"}
        Returns:
            (list): a list of web elements found
        """
        return self.driver.find_elements(locator["by"], locator["value"])

    def _type_text(self, text, locator):
        """
        Type the text string into the element identified by locator
        Args:
            text (str): the text to type
            locator (dict): the element's strategy to be located and the locator value
            e.g {"by": By.XPATH, "value": "//li[@class]"}
        """
        self._find_element(locator).send_keys(text)

    def _click_element(self, locator):
        """
        Clicks on a web element identified by locator
        Args:
            locator (dict): the element's strategy to be located and the locator value
            e.g {"by": By.XPATH, "value": "//li[@class]"}
        """
        self._find_element(locator).click()

    def _scroll_to_element(self, locator):
        """
        Scroll a web element identified by locator into view
        Args:
            locator (dict): the element's strategy to be located and the locator value
            e.g {"by": By.XPATH, "value": "//li[@class]"}
        """
        element = self._find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
