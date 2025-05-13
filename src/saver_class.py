import json
import os
from abc import ABC, abstractmethod

from src.hh_class import Vacancy


class BaseSave(ABC): # pragma: no cover
    @abstractmethod
    def __init__(self, data, name="vacancies"):
        self.data = data
        self.__name = name

    @abstractmethod
    def save_to_file(self):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass


class File_Save(BaseSave):
    """Класс для сохранения данных в файл для дальнейшей работы с ним,
    может также удалять все вакансии в файле, читать его, и добавлять вакансии отдельно"""

    def __init__(self, data, name="vacancies"):
        self.data = data
        self.__name = name

    def save_to_file(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "..", "data")
        file_path = os.path.join(data_dir, f"{self.__name}.json")
        new_data = {"items": []}
        for i in self.data["items"]:
            salary_from = 0
            salary_to = 0

            if i.get("salary"):
                salary_from = i["salary"].get("from") or 0
                salary_to = i["salary"].get("to") or 0

            vacancy = Vacancy(i["name"], i["alternate_url"], salary_from, salary_to, i["snippet"]["requirement"])
            new_data["items"].append(vacancy.main_data())

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=2)

    def read_file(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "..", "data")
        file_path = os.path.join(data_dir, f"{self.__name}.json")
        with open(file_path, encoding="utf-8") as r:
            file = json.load(r)
        return file

    def delete_vacancies(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "..", "data")
        file_path = os.path.join(data_dir, f"{self.__name}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump({}, f)

    def add_vacancy(self, vacancy):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "..", "data")
        file_path = os.path.join(data_dir, f"{self.__name}.json")
        if isinstance(vacancy,Vacancy):
            vacancy = vacancy.main_data()
            with open(file_path, encoding="utf-8") as r:
                data = json.load(r)
            if not any(v == vacancy for v in data['items']):
                data['items'].append(vacancy)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False,indent=2)
        else:
            print("Можно добавлять только main_data из класса Vacancy")
