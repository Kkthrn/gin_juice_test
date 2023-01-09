from seleniumbase import SeleniumBase


class LoginPageAuth(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_form: str = 'username'
        self.passwd_form: str = 'password'
        self.submit_btn: str = "//button[@class='button']"
        self.user_locator_field: str = "//div[@id='account-content']/p"
        self.invalid_data_warning: str = 'is-warning'

    def get_login_form(self):
        return self.is_visible('name', self.login_form, 'Login Form')

    def get_passwd_form(self):
        return self.is_visible('name', self.passwd_form, 'Password Form')

    def get_submit_btn(self):
        return self.is_visible('xpath', self.submit_btn, 'Submit Button')

    def get_user_locator_field(self):
        return self.is_visible('xpath', self.user_locator_field, 'User Locator Field')

    def get_invalid_data_warning(self):
        return self.is_visible('class_name', self.invalid_data_warning, 'Invalid Data Warning')

    def set_login_input(self, input_text: str):
        self.get_login_form().send_keys(input_text)

    def set_passwd_input(self, input_text: str):
        self.get_passwd_form().send_keys(input_text)

    def click_submit_btn(self):
        self.get_submit_btn().click()

    def get_text_from_user_locator_field(self):
        us_loc_field = self.get_user_locator_field()
        us_loc_field_text = us_loc_field.text
        return us_loc_field_text

    def get_text_from_invalid_data_warning(self):
        inv_data = self.get_invalid_data_warning()
        inv_data_text = inv_data.text
        return inv_data_text



