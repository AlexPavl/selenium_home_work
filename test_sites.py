import unittest
from selenium import webdriver
import time

class TestSites(unittest.TestCase):
    def mFunc(self, link):
        try:
            browser = webdriver.Chrome()
            browser.get(link)

            first_name = browser.find_element_by_xpath('//div[@class="first_block"]/div/label[text()="First name*"]/following-sibling::input')
            first_name.send_keys("Alex")
            last_name = browser.find_element_by_xpath('//div[@class="first_block"]/div/label[text()="Last name*"]/following-sibling::input')
            last_name.send_keys("Pav")
            email = browser.find_element_by_xpath('//div[@class="first_block"]/div/label[text()="Email*"]/following-sibling::input')
            email.send_keys("pukpukpuk@mail.ru")
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(1)
            welcome_text_elt = browser.find_element_by_tag_name('h1')
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            time.sleep(10)
            browser.quit()

    def test_link_1(self):
        self.mFunc("http://suninjuly.github.io/registration1.html")

    def test_link_2(self):
        self.mFunc("http://suninjuly.github.io/registration2.html")

if __name__ == "__main__":
    unittest.main()