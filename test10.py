from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select




link = "https://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'num1')
    x = x_element.text
    y_element = browser.find_element(By.ID, 'num2')
    y = y_element.text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(int(x)+int(y)))

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла