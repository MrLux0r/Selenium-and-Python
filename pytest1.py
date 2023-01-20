from selenium import webdriver
import unittest, time
from selenium.webdriver.common.by import By

def get_text(link):
    browser = webdriver.Chrome()
    browser.get(link)
    f_name = browser.find_element(By.CSS_SELECTOR,'[placeholder="Input your first name"]')
    f_name.send_keys("Ivan")
    l_name = browser.find_element(By.CSS_SELECTOR,'[placeholder="Input your last name"]')
    l_name.send_keys("Petrov")
    i_email = browser.find_element(By.CSS_SELECTOR,'[placeholder="Input your email"]')
    i_email.send_keys("Smolensk@qqqqq.ru")
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME ,"h1")
    welcome_text = welcome_text_elt.text
    browser.quit()
    return welcome_text

class TestAbs(unittest.TestCase):

    def test_link1(self):
        welcome_text = get_text("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_link2(self):
        welcome_text = get_text("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()

