class Vacancy:
    """Класс для создания вакансий и работы с ними,
    их можно сравнивать друг с другом, выводить в консоль,
    а также все зарплаты валидируються в специальном приватном методе"""

    __slots__ = ("__name", "url", "salary_from", "salary_to", "desc")

    def __init__(self, name, url, salary_from, salary_to, desc):
        self.__name = name
        self.url = url
        self.salary_from = self._validate_salary(salary_from)
        self.salary_to = self._validate_salary(salary_to)
        self.desc = desc

    @property
    def name(self):
        return self.__name

    def _validate_salary(self, value):
        """Приватный валидатор суммы денег"""
        if isinstance(value, (int, float)) and value > 0:
            return value
        return 0

    def main_data(self):
        """Возвращает всю информацию о вакансии как в json файле для работы с ним"""
        return {
            "name": self.__name,
            "alternate_url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "snippet": {"requirement": self.desc},
        }

    def __str__(self):
        return f"""    Название: {self.__name}
    Ссылка: {self.url}
    Зарплата от {self.salary_from} до {self.salary_to}
    Описание: {self.desc}"""

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        return self.salary_from != other.salary_from

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        return self.salary_from >= other.salary_from
