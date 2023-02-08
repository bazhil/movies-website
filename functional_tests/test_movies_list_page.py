from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from apps.movies.models import Movie
from django.urls import reverse
import time
import undetected_chromedriver as uc

class TestMoviesAdmin(StaticLiveServerTestCase):
    def setUp(self):
        # так не работает, тк браузер определяет селением и блокирует
        # https://www.appsloveworld.com/bestanswer/selenium/118/selenium-chromedriver-opening-a-blank-page
        # self.browser = webdriver.Chrome('functional_tests/chromedriver', options=options)
        self.browser = uc.Chrome()

    def tearDown(self):
        self.browser.close()

    def test_admin(self):

        self.browser.get(("%s%s" % (self.live_server_url, '/admin/')))
        self.assertEquals(
                self.browser.title,
                'Войти | Django Movies'
            )

class LoginFormTest(LiveServerTestCase):
    def test_login(self):
        browser = uc.Chrome()
        browser.get(("%s%s" % (self.live_server_url, 'http://127.0.0.1:8000/ru/accounts/login/')))

        time.sleep(2)

        user_name = browser.find_element(By.ID, 'id_login')
        user_password = browser.find_element(By.ID, 'id_password')
        submit = browser.find_element(By.CLASS_NAME, 'primaryAction')

        time.sleep(2)

        user_name.send_keys('admin')
        user_password.send_keys('123456')

        time.sleep(2)

        submit.send_keys(Keys.RETURN)

        assert 'admin' in browser.page_source
