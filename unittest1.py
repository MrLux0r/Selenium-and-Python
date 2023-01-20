from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


def test6_in_unittest(link):
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    # input1 = browser.find_element(By.CLASS_NAME, "form-control.first")Input your first name
    input1 = browser.find_element(By.CSS_SELECTOR,
                                  'form[action="registration_result.html"] .first_block .form-group.first_class .form-control.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR,
                                  '[action="registration_result.html"] .first_block .form-group.second_class .form-control.second')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR,
                                  'form[action="registration_result.html"] .first_block .form-group.third_class .form-control.third')
    input3.send_keys("Smolensk@gmail.com")
    input4 = browser.find_element(By.CSS_SELECTOR,
                                  'form[action="registration_result.html"] .second_block .form-group.first_class .form-control.first')
    input4.send_keys("My number")
    input5 = browser.find_element(By.CSS_SELECTOR,
                                  'form[action="registration_result.html"] .second_block .form-group.second_class .form-control.second')
    input5.send_keys("My address")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome = welcome_text_elt.text
    browser.quit()
    return welcome



class Test_Unittest(unittest.TestCase):
    def test1(self):
        self.assertEqual("Congratulations! You have successfully registered!",
                         test6_in_unittest("http://suninjuly.github.io/registration1.html"))

    def test2(self):
        self.assertEqual("Congratulations! You have successfully registered!",
                         test6_in_unittest("http://suninjuly.github.io/registration2.html"))



if __name__ == "__main__":
    unittest.main()