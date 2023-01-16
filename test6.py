from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    #input1 = browser.find_element(By.CLASS_NAME, "form-control.first")Input your first name
    input1 = browser.find_element(By.CSS_SELECTOR, 'form[action="registration_result.html"] .first_block .form-group.first_class .form-control.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '[action="registration_result.html"] .first_block .form-group.second_class .form-control.second')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'form[action="registration_result.html"] .first_block .form-group.third_class .form-control.third')
    input3.send_keys("Smolensk@gmail.com")

    input4 = browser.find_element(By.CSS_SELECTOR, 'form[action="registration_result.html"] .second_block .form-group.first_class .form-control.first')
    input4.send_keys("My number")
    input5 = browser.find_element(By.CSS_SELECTOR, 'form[action="registration_result.html"] .second_block .form-group.second_class .form-control.second')
    input5.send_keys("My address")

    # input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.first_class .form-control.first')
    # input1.send_keys("Ivan")
    # input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.third_class .form-control.third')
    # input2.send_keys("Smolensk@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()