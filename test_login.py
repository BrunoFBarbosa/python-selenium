from pages.common_page import CommonPage
from pages.invoice import Invoice
from pages.login import Login
from pytest import fixture
from selenium import webdriver
from utils.constants import CHROME_DRIVER_PATH


class TestUI:
    
    @fixture
    def _setup(self, request):
        self._driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self._common_page = CommonPage(self._driver)
        self._login = Login(self._driver)
        self._invoice = Invoice(self._driver)

        self._common_page._go_to("https://automation-sandbox.herokuapp.com/")

        def teardown():
            self._driver.quit()
        
        request.addfinalizer(teardown)
    
    @fixture(params=[("Demouser", "abc123"),
                     ("demouser_", "xyz"),
                     ("demouser", "nananana"),
                     ("demouser", "abc123"),
                     ])
    def _setup_invalid_users(self, request, _setup):
        self._username, self._password = request.param
        return self._username, self._password

    def test_valid_login(self, _setup):
        
        self._login.set_username("demouser")
        self._login.set_password("abc123")
        self._login.send_credentials()
        assert self._invoice.page_is_visible()
    
    def test_invalid_login(self, _setup_invalid_users):
        
        self._login.set_username(self._username)
        self._login.set_password(self._password)
        self._login.send_credentials()
        assert self._login.error_message_is_visible()
