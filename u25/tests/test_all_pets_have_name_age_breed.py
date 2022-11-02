from conftest import *


def test_all_pets_have_name_age_breed(go_to_my_pets):
    """Поверяем, что на странице со списком моих питомцев,
             у всех моих питомцев есть имя, возраст и порода"""
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody")))
    # Проверяем, что на странице "Мои питомцы" присутствуют все питомцы
    # Из всей таблицы питомцев
    pets_list = pytest.driver.find_element(By.XPATH, "//tbody")
    # Берем список питомцев
    each_pet = pets_list.find_elements(By.TAG_NAME, 'tr')
    # Создаем пустой список, куда будем помещать добытый циклом список элементов "Кличка", "Порода", "Возраст" для каждого питомца вперемешку
    pets_list_info = []
    for i in each_pet:
        pets_list_info.append(list(i.find_elements(By.TAG_NAME, 'td')))
    # Еще одним циклом получившийся список разбиваем на отдельные элементы "Кличка", "Возраст", "Порода"
    bad_pet = False

    for i in pets_list_info:
        pet_name = i[0].text
        pet_age = i[1].text
        pet_breed = i[2].text
        # Если какой-то из этих элементов пуст, то прерываем цикл
        if pet_name == "" or pet_age == "" or pet_breed == "":
            bad_pet = True
            break

    assert bad_pet == False


# python -m pytest -v --driver Chrome --driver-path C:\\chromedriver\\chromedriver.exe test_all_pets_have_name_age_breed.py
# Статистика на момент запуска теста: 1 вариант: Всего питомцев 9, с фото 4, без имени 0: ОР: PASSED  ФР: PASSED
#                                     2 вариант: Всего питомцев 10, с фото 5 из них без имени 1: ОР: FAILED  ФР: FAILED

