from pages.common_page import CommonPage
from selenium.webdriver.common.by import By


class Invoice(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
        self._invoice_header = {"by": By.XPATH, "value": '//h2[text()="Invoice List"]'}
        self._invoice_item_details = {"by": By.XPATH, "value": '//a[normalize-space()="Invoice Details"]'}

    def page_is_visible(self):
        """
        Verify the invoice page is visible
        Returns:
            (bool): whether the page is visible or not
        """
        return self._element_is_visible(self._invoice_header)
    
    def click_on_item_details(self, item):
        """
        Click on a specific item from the invoice list
        Args:
            item (int): the position of the invoice in the list, starting from 1
        """

        self._invoice_item_details["value"] = '({})[{}]'.format(self._invoice_item_details["value"], item)
        self._click_element(self._invoice_item_details)
