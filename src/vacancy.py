class Vacancy:
    '''Класс для организации данных по вакансиям в удобном виде. хранит в себе полезные атрибуты по вакансиям'''
    def __init__(self, id_, region, name, salary, currency, requirement, vacancy_url):
        self.id_ = id_
        self.region = region if region else "не указано"
        self.name = name
        self.salary = salary if salary else 0
        self.currency = currency if self.validate(currency) else ''
        self.requirement = requirement
        self.vacancy_url = vacancy_url

    def __str__(self):
        """строковое представление для пользователя"""
        return f'''id:{self.id_}, Регион: {self.region}, Вакансия: {self.name}, Зарплата: {self.salary} {self.currency}, 
        Требования: {self.requirement}
        ссылка на вакансию: {self.vacancy_url}'''

    # def __repr__(self):
    #     return f"{self.name} {self.salary}"

    def __lt__(self, other):
        """сравнение self < other"""
        if self.salary is not None and other.salary is not None:
            return self.salary < other.salary

    @staticmethod
    def validate(currency):
        """проверка зарплаты в рублях"""
        if currency in ["rub", "RUR"]:
            return True
        else:
            return False

#a = Vacancy('101276173', 'Russia','Junior Python разработчик', 10000, 'RU', '', '')
#b = {'id': '101276173', 'premium': False, 'name': 'Junior Python разработчик / IT / (удаленно)', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': {'from': 70000, 'to': 100000, 'currency': 'RUR', 'gross': False}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-06-04T16:05:31+0300', 'created_at': '2024-06-04T16:05:31+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=101276173', 'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/101276173?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/101276173', 'relations': [], 'employer': {'id': '5856776', 'name': 'Зерокодер', 'url': 'https://api.hh.ru/employers/5856776', 'alternate_url': 'https://hh.ru/employer/5856776', 'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/4218197.jpeg', '90': 'https://img.hhcdn.ru/employer-logo/4218196.jpeg', 'original': 'https://img.hhcdn.ru/employer-logo-original/944415.jpeg'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=5856776', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Уверенное владение <highlighttext>Python</highlighttext>, Django. - Опыт работы с СУБД PostgreSQL, MySQL, Redis. - Умение работать с фреймворками FastAPI, Flask. - Свободное владение Linux. - ', 'responsibility': 'Разработка и поддержка программного обеспечения ( с нейросетями и без). - Работа с базами данных. - Тестирование кода. - Интеграция различных компонентов и модулей. - '}, 'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}
#c = Vacancy(**b)
