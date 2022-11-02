from conftest import *
from collections import Counter


def test_pets_have_different_names(go_to_my_pets):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody")))
    # Проверяем, что на странице "Мои питомцы" присутствуют все питомцы
    pets_list = pytest.driver.find_element(By.XPATH, "//tbody")
    each_pet = pets_list.find_elements(By.TAG_NAME, 'tr')
    # Создаем пустой список питомцев, куда с помощью цикла будем класть имена питомцев
    pet_names = []

    for i in each_pet:
        pet_names.append(i.find_element(By.TAG_NAME, 'td').text)

    assert len(Counter(pet_names)) == len(each_pet)


# python -m pytest -v --driver Chrome --driver-path C:\\chromedriver\\chromedriver.exe test_pets_have_different_names.py
# Статистика на момент запуска теста: 1 вариант: Всего питомцев 4, с фото 3, без имени 0: ОР: PASSED  ФР: PASSED
#                                     2 вариант: Всего питомцев 5, с фото 4, двое с одинаковыми именами: ОР: FAILED  ФР: FAILED
