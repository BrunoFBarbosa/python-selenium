from pages import common_page, invoice, invoice_details, login
from pytest import fixture
from selenium import webdriver
from utils.constants import CHROME_DRIVER_PATH


class TestInvoice:
    
    @fixture
    def _setup(self, request):
        
        self._driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self._common_page = common_page.CommonPage(self._driver)
        self._login = login.Login(self._driver)
        self._invoice = invoice.Invoice(self._driver)
        self._invoice_details = invoice_details.InvoiceDetails(self._driver)
        
        self._common_page._go_to("https://automation-sandbox.herokuapp.com/")
        self._login.set_username("d³emouser")
        self._login.set_password("abc123")
        self._login.send_credentials()

        def teardown():
            self._driver.quit()
        
        request.addfinalizer(teardown)

    def test_valid_invoice_details(self, _setup):
        
        self._invoice.click_on_item_details(1)
        # switching the driver context to the new opened tab
        self._driver.switch_to.window(self._driver.window_handles[1])
        assert self._invoice_details.page_is_visible()
        
        assert self._invoice_details.invoice_hotel_name_is_visible("Rendezvous Hotel")
        assert self._invoice_details.invoice_date_is_visible("14/01/2018")
        assert self._invoice_details.invoice_due_date_is_visible("15/01/2018")
        assert self._invoice_details.invoice_number_is_visible("110")

        assert self._invoice_details.invoice_table_row_is_visible("Booking Code", "0875")
        assert self._invoice_details.customer_details_should_have(['JOHNY SMITH', 'R2, AVENUE DU MAROC', '123456'])
        assert self._invoice_details.invoice_table_row_is_visible("Room", "Superior Double")
        assert self._invoice_details.invoice_table_row_is_visible("Check In", "14/01/2018")
        assert self._invoice_details.invoice_table_row_is_visible("Check Out", "15/01/2018")
        assert self._invoice_details.invoice_table_row_is_visible("Total Stay Count", "1")
        assert self._invoice_details.invoice_table_row_is_visible("Total Stay Amount", "$150")

        assert self._invoice_details.invoice_billing_details_is_visible("Deposit Now", "USD $20.90", 0)
        assert self._invoice_details.invoice_billing_details_is_visible("Tax & VAT", "USD $19.00", 1)
        assert self._invoice_details.invoice_billing_details_is_visible("Total Amount", "USD $209.00", 2)
