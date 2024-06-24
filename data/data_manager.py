import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class DataSaver(ABC):
    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def save_vacancy(self):
        pass

    @abstractmethod
    def delete_vacancy_by_id(self):
        pass


class JSONSaver(Vacancy):
    """класс для работы с файлом"""
    def __init__(self, file_name='data.json'):
        self.file_name = file_name

    def read_vacancies(self):
        with open(self.file_name, 'r') as file:
            data = json.load(file)
            return data

    def save_vacancy(self, data):
        '''сохраняет экземпляры вакансий в файл'''
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_vacancy_by_id(self):
        pass

# a = JSONSaver()
#
# b = HHApi()
# c = VacanciesParser()
#
# b.load_vacancies('', 2)
# vacancies_list = b.vacancies
# parse_vac_list = c.parser_api_vacancies(vacancies_list)
# print(*parse_vac_list, sep='\n')
# a.save_vacancy(parse_vac_list)
