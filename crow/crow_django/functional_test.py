from selenium import webdriver
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        # self.browser = webdriver.Firefox()
        # Headless test using phantomjs driver
        self.browser = webdriver.PhantomJS('phantomjs')

        # The browsers window-size is set to a desktop resolution
        self.browser.set_window_size(1024, 768)

    def tearDown(self):
        self.browser.quit()

    def test_can_view_an_open_layers_map(self):
        # The GIS community has heard of a new tool to analyse a quarter.
        # Mr. Leo Graphy opens his webbrowser and opens the url.
        self.browser.get(self.live_server_url)

        # He expects to find a page where he can logins
        self.assertIn('Open eQuarter - Login', self.browser.title)

        # A login form is available to enter his username and password
        login_username = self.browser.find_element_by_id('id_username')
        login_password = self.browser.find_element_by_id('id_password')

        self.assertEqual(login_username.get_attribute('placeholder'), 'Username')
        self.assertEqual(login_password.get_attribute('placeholder'), 'Password')


        # a link is found, which leads those users who do not have an account yet to a page, where they can register
        register_link = self.browser.find_element_by_partial_link_text('egister')
        self.assertIsNotNone(register_link)

        # Leo does not have an account and therefore has to create one first
        register_link.click()

        # Again a form is displayed, which allows a new user to create an account
        reg_username = self.browser.find_element_by_id('id_username')
        reg_email = self.browser.find_element_by_id('id_email')
        reg_password1 = self.browser.find_element_by_id('id_password1')
        reg_password2 = self.browser.find_element_by_id('id_password2')

        self.assertEqual(reg_username.get_attribute('placeholder'), 'Username')
        self.assertEqual(reg_email.get_attribute('placeholder'), 'Email')
        self.assertEqual(reg_password1.get_attribute('placeholder'), 'Password')
        self.assertEqual(reg_password2.get_attribute('placeholder'), 'Password confirmation')

        # Desperate to use the platform, he decides on a username and a password and creates an account
        reg_username.send_keys('LeoGraphy')
        reg_email.send_keys('leo.graphy@ema.il')
        reg_password1.send_keys('LeosPW1234')
        reg_password2.send_keys('LeosPW1234')

        buttons = self.browser.find_elements_by_tag_name('button')
        reg_button = list(filter(lambda button: button.get_attribute('type') == 'submit', buttons))[0]
        reg_button.click()

        # The user is forwarded to a page, which confirms the registration
        self.assertIn('Open eQuarter - Success!', self.browser.title)
