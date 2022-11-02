from conftest import *
from collections import Counter


def test_no_duplicate_pets(go_to_my_pets):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody")))
    # Проверяем, что на странице "Мои питомцы" присутствуют все питомцы
    pets_list = pytest.driver.find_element(By.XPATH, "//tbody")
    each_pet = pets_list.find_elements(By.TAG_NAME, 'tr')

    pets_list_info = []
    for i in each_pet:
        separated_pets_attribute = i.find_elements(By.TAG_NAME, 'td')
        name = separated_pets_attribute[0].text
        age = separated_pets_attribute[1].text
        breed = separated_pets_attribute[2].text

        pets_list_info.append(name + age + breed)

    print(Counter(pets_list_info))

    assert len(Counter(pets_list_info)) == len(pets_list_info)

# python -m pytest -v --driver Chrome --driver-path C:\\chromedriver\\chromedriver.exe test_no_duplicate_pets.py
# Статистика на момент запуска теста: 1 вариант: Всего питомцев 3, с фото 3, без имени 0: ОР: PASSED  ФР: PASSED
#                                     2 вариант: Всего питомцев 4, с фото 4, двое одинаковы: ОР: FAILED  ФР: FAILED
