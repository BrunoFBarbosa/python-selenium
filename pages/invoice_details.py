from pages.common_page import CommonPage
from selenium.webdriver.common.by import By


class InvoiceDetails(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
        self._invoice_details_header = {"by": By.XPATH, "value": '//h2[text()="Invoice Details"]'}
        self._hotel_name = {"by": By.XPATH, "value": '//h4[normalize-space()="{}"]'}
        self._invoice_date = {"by": By.XPATH, "value": '//li[normalize-space()="Invoice Date: {}"]'}
        self._due_date = {"by": By.XPATH, "value": '//li[normalize-space()="Due Date: {}"]'}
        self._invoice_number = {"by": By.XPATH, "value": '//h6[normalize-space()="Invoice #{} details"]'}

        self._table_row_property = {"by": By.XPATH,
                                    "value": '//td[normalize-space()="{}"]'
                                             '//following-sibling::td[normalize-space()="{}"]'}
        self._billing_details_table_header = {"by": By.XPATH,
                                              "value": '//h5[normalize-space()="Billing Details"]'
                                                       '//following-sibling::table//thead//td'}
        self._billing_details_table_values = {"by": By.XPATH,
                                              "value": '//h5[normalize-space()="Billing Details"]'
                                                       '//following-sibling::table//tbody//td'}
        self._customer_info = {"by": By.XPATH,
                               "value": '//h5[normalize-space()="Customer Details"]//following-sibling::div'}

    def page_is_visible(self):
        """
        Verify if the invoice details page is visible
        Returns:
            (bool): whether the page is visible or not
        """
        return self._element_is_visible(self._invoice_details_header)

    def invoice_hotel_name_is_visible(self, hotel_name):
        """
        Validate the hotel_name is visible in the invoice
        Args:
            hotel_name (str): the hotel's name
        Returns:
            (bool): whether the hotel name is visible or not
        """
        self._hotel_name["value"] = self._hotel_name["value"].format(hotel_name)
        return self._element_is_visible(self._hotel_name)

    def invoice_date_is_visible(self, date):
        """
        Validate the date is visible in the invoice
        Args:
            date (str): the date to search for, in the format dd/mm/yyyy
        Returns:
            (bool): whether the date is visible or not
        """
        self._invoice_date["value"] = self._invoice_date["value"].format(date)
        return self._element_is_visible(self._invoice_date)

    def invoice_due_date_is_visible(self, date):
        """
        Validate the due date is visible in the invoice
        Args:
            date (str): the date to search for, in the format dd/mm/yyyy
        Returns:
            (bool): whether the due date is visible or not
        """
        self._due_date["value"] = self._due_date["value"].format(date)
        return self._element_is_visible(self._due_date)

    def invoice_number_is_visible(self, number):
        """
        Validate the invoice number is visible in the invoice
        Args:
            number (str): the invoice number to search for
        Returns:
            (bool): whether the invoice number is visible or not
        """
        self._invoice_number["value"] = self._invoice_number["value"].format(number)
        return self._element_is_visible(self._invoice_number)

    def invoice_table_row_is_visible(self, row, value):
        """
        Validate the invoice table contains the desired value
        Args:
            row (str): the table's row
            value (str): the table's value that row should have
        Returns:
            (bool): whether the table row contains the desired value or not
        """
        self._table_row_property["value"] = self._table_row_property["value"].format(row, value)
        return self._element_is_visible(self._table_row_property)

    def customer_details_should_have(self, data):
        """
         Verify the customer details are visible.
         This method extracts the customer info in the web page and
         creates a list where the customer's name is in the first position,
         the street address is the second, and the number is the third, e.g [name, street_address, number]
         Args:
             data (list): the customer's info, e.g [name, street_address, number]
        Returns:
            (bool): whether the customer's info is equal to data
         """
        element = self._find_element(self._customer_info)
        customer_info = element.text.split("\n")
        return customer_info == data

    def invoice_billing_details_is_visible(self, column, value, position):
        """
        Verify that the billing table contains the desired value in the column
        E.g:
              0            1           2
        | Deposit Now | Tax&VAT | Total Amount
        | USD $20.90  | USD $19 | USD $209

        If we want to check whether the Deposit Now column has the value of 20.90 or not
        column = Deposit Now
        value = 20.90
        position = 0 (first column)

        If we want to check whether the Tax&VAT column has the value of 19 or not
        column = Tax&VAT
        value = 19
        position = 1 (second column)
        Args:
            column (str): the column's name to verify
            value (str): the value that column should have
            position (int): the position on the table that column and value should be, starting from 0
        Returns:
            (bool): whether the table column has the value in the expected position
        """
        head_rows = self._find_elements(self._billing_details_table_header)
        values_rows = self._find_elements(self._billing_details_table_values)

        # extract the text from the table header and values webelements
        head_rows_list = [entry.text for entry in head_rows]
        values_rows_list = [values.text for values in values_rows]

        return head_rows_list[position] == column and values_rows_list[position] == value
