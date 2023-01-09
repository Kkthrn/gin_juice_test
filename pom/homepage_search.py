from seleniumbase import SeleniumBase


class HomepageSearch(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.search_input: str = 'search'
        self.search_button: str = "//button[@class='button']"
        self.blog_header: str = "//div[@class='blog-post']/h2"

    def get_search_input(self):
        return self.is_visible('name', self.search_input, 'Search Input')

    def get_search_button(self):
        return self.is_visible('xpath', self.search_button, 'Search Button')

    def get_blog_header(self):
        return self.is_visible('xpath', self.blog_header, 'Blog Header')

    def set_search_input(self, input_text: str):
        self.get_search_input().send_keys(input_text)

    def get_(self):
        return self.is_visible('name', self.search_input, 'Search Input')

    def click_search_button(self):
        self.get_search_button().click()

    def get_text_from_blog_header(self):
        header = self.get_blog_header()
        header_text = header.text
        return header_text
