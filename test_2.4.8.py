from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
import time

driver = webdriver.Chrome()

try:
    # открыть сайт по ссылке
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    driver.get(link)

    # кликнуть на кнопку, когда price == 100
    book = driver.find_element_by_id('book')
    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    book.click()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = int(driver.find_element_by_id('input_value').text)
    value = log(abs(12 * sin(x)))
    answer = driver.find_element_by_id('answer')
    # ввод ответа на задачу
    answer.send_keys(str(value))
    submit = driver.find_element_by_xpath('.//button[text()="Submit"]')
    submit.click()

    # глупое ожидание для копирования значения для ответа из модального окна
    time.sleep(10)
finally:
    driver.quit()