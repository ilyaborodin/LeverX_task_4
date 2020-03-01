import json


class JsonReader:
    """Класс служит для считывания информации с json файлов и преобразования
    ее в сущности Room и Student"""
    def load_json_file(self, path: str):
        try:
            with open(path, 'r', encoding='utf-8') as file:
                json_list = json.load(file)
        except FileNotFoundError:
            raise Exception("Не найден файл по указаному пути: {0}".format(path))
        except json.decoder.JSONDecodeError:
            raise Exception("Неверный формат json")
        return json_list
