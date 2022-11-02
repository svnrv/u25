import os
import time
import uuid
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains  # симуляции нажатия клавиш на клавиатуре
from selenium.webdriver.common.keys import Keys  # симуляции нажатия клавиш на клавиатуре
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


@pytest.fixture()
def go_to_my_pets():
    # Устанавливаем явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    
    # Устанавливаем явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Устанавливаем явное ожидание для входа в аккаунт
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Устанавливаем явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.navbar-toggler-icon')))
    # Нажимаем на кнопку навигатор-бар(для формата окна  1400*800)
    pytest.driver.find_element(By.CSS_SELECTOR, 'span.navbar-toggler-icon').click()

    # Устанавливаем явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Мои питомцы")]')))
    # Нажимаем на кнопку Мои питомцы
    pytest.driver.find_element(By.XPATH, '//a[contains(text(), "Мои питомцы")]').click()
 

