from data.data_manager import JSONSaver
from src.utils import get_top_vacancies, get_vacancies_by_salary, sort_vacancies, filter_vacancies
from src.vacancy import Vacancy


def test_read_file():
    """тест на чтение файла"""
    saver = JSONSaver('test_json_read.json')
    data = saver.read_vacancies()
    expected = [
        {
            "id_number": "102404974",
            "region": "Ростов-на-Дону",
            "name": "Стажер-разработчик Python",
            "filtered_salary": 100000,
            "currency": "RUR",
            "requirement": "Мы ищем Python-разработчика, уровнем от Junior и выше, желательно с опытом развития новых продуктов. Уверенные знания Python 3.8...",
            "vacancy_url": "https://hh.ru/vacancy/102404974"
        }
    ]
    assert data == expected


inst_1 = Vacancy('12', 'Москва', 'Python', 20000, 'RUR', 'afdg', 'aerg')
inst_2 = Vacancy('124', 'Киев', 'Python', 60000, 'RUR', 'afdg', 'aerg')
inst_3 = Vacancy('122', 'Уфа', 'Python', 70000, 'RUR', 'afdg', 'aerg')
vac_list = [inst_1, inst_2, inst_3]


def test_get_top_vacancies():
    """тест на топ вакансий"""
    data = get_top_vacancies(vac_list, 2)
    expected = [inst_1, inst_2]
    assert data == expected


def test_get_vacancies_by_salary():
    """тест на получение вакансий по зарплате"""
    data = get_vacancies_by_salary(vac_list, 50000, 80000)
    expected = [inst_2, inst_3]
    assert data == expected


def test_sort_vacancies():
    """тест на сортировку вакансий"""
    data = sort_vacancies(vac_list)
    expected = [inst_3, inst_2, inst_1]

    assert data == expected


def test_filter_vacancies():
    """тест на фильтрацию вакансий по слову"""
    data = filter_vacancies(vac_list, 'Москва')
    expected = [inst_1]

    assert data == expected
