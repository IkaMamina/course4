import requests
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class Api(ABC):
    @abstractmethod
    def load_vacancies(self, *args):
        pass


class HHApi(Api):
    """Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать"""
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword: str, page_quantity: int = 2):
        '''загружает данные c АПИ'''

        self.params['text'] = keyword
        while self.params.get('page') != page_quantity:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

# a = HHApi()
# a.load_vacancies('Python', 1)
# print(a.vacancies)

class VacanciesParser:
    """Класс для парсинга данных с АПИ"""
    def parser_api_vacancies(self, vacancies: list):
        '''парсит данные c апи по определенным критериям'''
        vacancies_list = []

        for vacancy in vacancies:
            name = vacancy.get("name")
            salary = vacancy.get("salary")
            if salary and salary.get("from"):
                filtered_salary = salary["from"]
            else:
                filtered_salary = 0
            snippet = vacancy.get("snippet")
            if salary:
                salary = vacancy.get("salary")
                currency = salary.get("currency")
            else:
                currency = ''
            requirement = snippet.get("requirement")
            if requirement:
                requirement = requirement.replace('<highlighttext>', '').replace('</highlighttext>', '')
            else:
                requirement = "нет требований"
            vacancy_url = vacancy.get("alternate_url")
            area = vacancy.get("area")
            region = area.get("name")

            id_number = vacancy.get("id")
            vacancy_dict = {"id_number": id_number, "region": region, "name": name,
                           "filtered_salary": filtered_salary, "currency": currency,
                            "requirement": requirement, "vacancy_url": vacancy_url}

            vacancies_list.append(vacancy_dict)
        return vacancies_list

    def make_vacancies_instance(self, vacancies_list):
        vacancies_lst = []
        for vacancy in vacancies_list:
            vac_inst = Vacancy(vacancy['id_number'], vacancy["region"],vacancy["name"], vacancy['filtered_salary'], vacancy['currency'], vacancy['requirement'], vacancy['vacancy_url'])
            vacancies_lst.append(vac_inst)
        return vacancies_lst