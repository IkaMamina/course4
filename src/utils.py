from src.vacancy import Vacancy


def filter_vacancies(vacancies=Vacancy, word=None):
    """фильтрует вакансии по ключевому слову"""


    filtred_vacancies = []
    for vacancy in vacancies:
        if word in vacancy.region or word in vacancy.name or word in vacancy.requirement:
            filtred_vacancies.append(vacancy)
    return filtred_vacancies


def get_top_vacancies(vacancies, quantity: int = 10):
    """возвращает топ N вакансий"""
    return vacancies[:quantity]

def sort_vacancies(vacancies_list):
    """сортирует вакансии по зарплате"""
    return sorted(vacancies_list, reverse=True)


def get_vacancies_by_salary(vacancies, salary_min: int, salary_max: int):
    """получаем вакансии по диапазону зарплат"""
    catched = 0
    filtred_list = []
    for vacancy in vacancies:
        if salary_min <= vacancy.salary <= salary_max:
            filtred_list.append(vacancy)
            catched += 1
            if catched != 0:
                print(f"количество совпадений {catched}")

            else:
                print(f"зарплаты в диапазоне '{salary_min}' - '{salary_max}' отсутствуют, сбрось фильтр!")
    return filtred_list
