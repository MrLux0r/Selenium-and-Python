import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_options = Options()
    chrome_options.add_argument("--headless") # мы не видим открытие окон
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="session")
def start(): # первым делом создаем/очищаем logfile.txt
    print("\nstart cleaning logfile..")
    with open("logfile.txt", "w", encoding="utf-8") as f: #лог файл будет создан в той же директории
        f.write("")
    print("\nfinish cleaning logfile..")

@pytest.mark.parametrize('lesson', ['895', '896', '897', '898', '899', '903', '904', '905'])
def test_lesson_link(browser, lesson, start):
    browser.implicitly_wait(10)
    browser.get(f'https://stepik.org/lesson/236{lesson}/step/1')
    browser.find_element(By.CSS_SELECTOR, ".textarea").send_keys(math.log(int(time.time())))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))).click()
    check_text = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    print(check_text)
    if check_text != "Correct!":
        with open("logfile.txt", "a", encoding="utf-8") as f: # дозаписываем в logfile
            f.write(check_text + " ")
    assert check_text == "Correct!", "Optional feedback is not correct! see logfile.txt"


# Почему то тест не выводит текст в файл, код чисто для примера!