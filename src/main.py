from data.data_manager import JSONSaver
from src.api import HHApi, VacanciesParser
from src.utils import filter_vacancies, get_vacancies_by_salary, get_top_vacancies, sort_vacancies

hh_api = HHApi()
""""Создание экземпляра класса для работы с API сайтов с вакансиями"""
json_saver = JSONSaver()
"""Сохранение информации о вакансиях в файл"""

data_manager = JSONSaver()

def user_interaction():
    """Функция для взаимодействия с пользователем"""
    print('Привет!\n')
    search_query = input("Введите поисковый запрос (название вакансии):\n ")
    parser_instance = VacanciesParser()
    hh_api.load_vacancies(search_query)
    vacancies_list = hh_api.vacancies

    hh_vacancies = parser_instance.parser_api_vacancies(vacancies_list)
    data_manager.save_vacancy(hh_vacancies)
    vac_dict_list = data_manager.read_vacancies()
    vac_instance_list = parser_instance.make_vacancies_instance(vac_dict_list)

    print(*vac_instance_list, sep='\n')

    top_n = int(input("Введите количество вакансий для вывода в топ N:\n "))
    sorted_vac = sort_vacancies(vac_instance_list)
    top_vacancies = get_top_vacancies(vacancies=sorted_vac, quantity=top_n)
    print(*top_vacancies, sep='\n')

    filter_words = input("Введите ключевые слова для фильтрации вакансий:\n")
    filter_vac = filter_vacancies(vacancies=vac_instance_list, word=filter_words)
    print(*filter_vac, sep='\n')

    salary_range_min = int(input("Введите минимальный диапазон зарплат:\n "))
    salary_range_max = int(input("Введите максимальный диапазон зарплат:\n "))
    ranged_vacancies = get_vacancies_by_salary(vacancies=vac_instance_list, salary_min=salary_range_min, salary_max=salary_range_max)
    print(*ranged_vacancies, sep='\n')
    print('Удачи в поиске!')

if __name__ == "__main__":
    user_interaction()
