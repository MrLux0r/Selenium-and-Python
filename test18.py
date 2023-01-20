import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_guest_should_see_login_link(browser, language):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{language}/step/1"
    browser.get(link)
    time.sleep(5)
    q = browser.find_element(By.XPATH, '//*[@id="ember33"]')
    q.click()
    email = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
    email.send_keys("Тут ваш логин")
    par = browser.find_element(By.XPATH, '//*[@id="id_login_password"]')
    par.send_keys("Тут ваш пароль")
    button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader")
    button.click()
    time.sleep(5)

    pole = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area.ember-view.textarea.string-quiz__textarea")
    pole.send_keys(str(answer))
    button_site = browser.find_element(By.CSS_SELECTOR, ".attempt__actions .submit-submission")
    button_site.click()

    search_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints.ember-view.lesson__hint .smart-hints__hint')))
    text = search_text.text
    assert text != "Correct!", text

#Тест полностью рабочий только трудности с выводом текста хз почему, ответ я написал ниже! Это для удобства!

################# П.С вот ответ на это задание: <The owls are not what they seem! ovo>   ###########################





