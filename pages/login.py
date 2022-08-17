from pages.common_page import CommonPage
from selenium.webdriver.common.by import By


class Login(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
        self._username_field = {"by": By.NAME, "value": 'username'}
        self._password_field = {"by": By.NAME, "value": 'password'}
        self._login_button = {"by": By.ID, "value": 'btnLogin'}
        self._login_error_message = {"by": By.XPATH,
                                     "value": '//div[@role="alert" and normalize-space()="Wrong username or password."]'}

    def set_username(self, username):
        """
        Fill the username in the login page
        Args:
            username (str): the username to login in the system
        """
        self._type_text(username, self._username_field)

    def set_password(self, password):
        """
        Fill the password in the login page
        Args:
            password (str): the password of the user to login in the system
        """
        self._type_text(password, self._password_field)

    def send_credentials(self):
        """
        Click the Login button in the login page
        """
        self._click_element(self._login_button)
    
    def error_message_is_visible(self):
        """
        Verify the login error message is visible
        """
        return self._element_is_visible(self._login_error_message)
