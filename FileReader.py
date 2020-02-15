import json
from Rooms import Room
from Students import Student


class JSONReader:
    def _load_json_file(self, path: str) -> list:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                json_text = json.load(file)
        except FileNotFoundError:
            raise Exception("Не найден файл по указаному пути: {0}".format(path))
        except json.decoder.JSONDecodeError:
            raise Exception("Неверный формат json")
        return json_text

    def get_rooms(self, path: str) -> list:
        json_list = self._load_json_file(path)
        rooms = []
        for json_room in json_list:
            rooms.append(Room(json_room["id"], json_room["name"]))
        return rooms

    def get_students(self, path: str) -> list:
        json_list = self._load_json_file(path)
        students = []
        for json_student in json_list:
            students.append(Student(json_student["id"], json_student["name"], json_student["birthday"],
                                    json_student["room"], json_student["sex"]))
        return students