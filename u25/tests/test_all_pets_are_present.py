from conftest import *


def test_all_pets_are_present(go_to_my_pets):
   """Проверяем что на странице со списком моих питомцев присутствуют все мои питомцы """
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody")))
   # Проверяем, что на странице "Мои питомцы" присутствуют все питомцы
   # Из всей таблицы питомцев
   pets_list = pytest.driver.find_element(By.XPATH, "//tbody")
   # Вычленяем список питомцев из этой таблицы, каждый из элементов лежит в тегах 'tr'
   pets_list_info = pets_list.find_elements(By.TAG_NAME, 'tr')
   # Добываем число, находящееся в блоке слева напротив слова "Питомцев: "
   number_of_pets = pytest.driver.find_element(By.XPATH, "(//div[@class='.col-sm-4 left'])[1]").text.replace("\n", "").split(": ")[1].split("Друзей")[0]
   # Убеждаемся, что мы добыли его верно
   print(number_of_pets)
   # Сравниваем длину списка питомцев из таблицы с числом из блока слева
   assert len(pets_list_info) == int(number_of_pets)




# python -m pytest -v --driver Chrome --driver-path C:\\chromedriver\\chromedriver.exe test_all_pets_are_present.py
