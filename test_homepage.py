import pytest
from pom.homepage_search import HomepageSearch


@pytest.mark.usefixtures('setup_homepage')
class TestHomepage:

    def test_homepage_search(self, get_webdriver):
        self.driver = get_webdriver
        homepage_search = HomepageSearch(self.driver)
        homepage_search.set_search_input('hairy')
        homepage_search.click_search_button()
        assert 'Hairy' in homepage_search.get_text_from_blog_header()
