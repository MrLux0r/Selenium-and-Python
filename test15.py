from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from selenium.webdriver.common.keys import Keys

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)


    search_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'100')
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    browser.find_element(By.TAG_NAME,'body').send_keys(Keys.END)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(int(x))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button_last = browser.find_element(By.ID, "solve")
    button_last.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла