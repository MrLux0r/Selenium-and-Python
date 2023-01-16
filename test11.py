from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input1.send_keys(y)
    button_checkbox = browser.find_element(By.ID, "robotCheckbox")
    button_checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла