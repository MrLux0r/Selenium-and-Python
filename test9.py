from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'treasure')
    robots_checked = x_element.get_attribute("valuex")
    x = robots_checked
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button_Checkbox = browser.find_element(By.ID, "robotCheckbox")
    button_Checkbox.click()
    button_checkbox = browser.find_element(By.ID, "robotsRule")
    button_checkbox.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла