from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '.form-group #input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-group .form-control")
    input1.send_keys(y)
    button_checkbox = browser.find_element(By.CSS_SELECTOR, ".form-check.form-check-custom #robotCheckbox")
    button_checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, ".form-check.form-radio-custom #robotsRule")
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла