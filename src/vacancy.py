class Vacancy:
    '''Класс для организации данных по вакансиям в удобном виде. хранит в себе полезные атрибуты по вакансиям'''
    def __init__(self, id_, region, name, salary, currency, requirement, vacancy_url):
        self.id_ = id_
        self.region = region if region else "не указано"
        self._name = name
        self.salary = salary if salary else 0
        self.currency = currency if self.validate(currency) else ''
        self.requirement = requirement
        self.vacancy_url = vacancy_url

    def __repr__(self):

        return f"{self._name} {self.salary}"

    def __str__(self):
        """строковое представление для пользователя"""
        return f'''id:{self.id_}, Регион: {self.region}, Вакансия: {self._name}, Зарплата: {self.salary} {self.currency}, 
        Требования: {self.requirement}
        ссылка на вакансию: {self.vacancy_url}'''

    def __lt__(self, other):
        """сравнение self < other"""
        if self.salary is not None and other.salary is not None:
            return self.salary < other.salary

    @staticmethod
    def _validate(currency):
        """проверка зарплаты в рублях"""
        if currency in ["rub", "RUR"]:
            return True
        else:
            return False
