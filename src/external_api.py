from abc import ABC, abstractmethod

import requests


class BaseAPI(ABC):  # pragma: no cover

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _get_vacancies(self, desc, top_N=100):
        pass


class API_HH(BaseAPI):
    """Класс для работы с HeadHunterAPI, загружает вакансии из hh.ru json файлом"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"

    def _get_vacancies(self, desc, top_N=100):
        """Возвращает вакансии по поиску и сколько первых вакансий показать"""
        params = {"text": desc, "per_page": top_N, "search_field": "name"}
        vacancies = requests.get(url=self.__url, params=params)
        if vacancies.status_code != 200:
            print(f"Ошибка при работе с API запросом ошибка: {vacancies.status_code}")
        else:
            return vacancies.json()
