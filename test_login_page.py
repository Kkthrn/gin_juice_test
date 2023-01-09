import pytest
from pom.login_page_auth import LoginPageAuth


@pytest.mark.usefixtures('setup_login_page')
class TestHomepage:

    def test_login_page_valid(self, get_webdriver):
        self.driver = get_webdriver
        login_page_auth = LoginPageAuth(self.driver)
        login_page_auth.set_login_input('carlos')
        login_page_auth.set_passwd_input('hunter2')
        login_page_auth.click_submit_btn()
        assert login_page_auth.get_text_from_user_locator_field() == 'Your username is: carlos'

    def test_login_page_invalid(self, get_webdriver):
        self.driver = get_webdriver
        login_page_auth = LoginPageAuth(self.driver)
        login_page_auth.set_login_input('admin')
        login_page_auth.set_passwd_input('admin')
        login_page_auth.click_submit_btn()
        assert login_page_auth.get_text_from_invalid_data_warning() == 'Invalid username or password.'


