from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from apps.movies.models import Movie
from django.urls import reverse
import time


class TestMoviesListPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver')

    def tearDown(self):
        self.browser.close()

    def test_no_projects_alert_is_displayed(self):
        # TODO: разобраться с современными способами тестировать на селениум!
        self.browser.get(self.live_server_url)

        # The user requests the page for the first time
        alert = self.browser.find_element_by_class_name('banner-info')
        self.assertEquals(
            alert.find_element_by_tag_name('p').text,
            'лучший сайт на django 3'
        )