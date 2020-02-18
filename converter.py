import students
import rooms


class Converter:
    def from_list_to_rooms(self, json_list: list) -> list:
        rooms_list = []
        for json_room in json_list:
            rooms_list.append(rooms.Room(json_room["id"], json_room["name"]))
        return rooms_list

    def from_list_to_students(self, json_list: list) -> list:
        students_list = []
        for json_student in json_list:
            students_list.append(students.Student(json_student["id"], json_student["name"], json_student["birthday"],
                                 json_student["room"], json_student["sex"]))
        return students_list

    def from_tuples_to_rooms(self, tuple_of_rooms: list) -> list:
        rooms_list = []
        for tuple_of_room in tuple_of_rooms:
            rooms_list.append(rooms.Room(id=tuple_of_room[0],
                              name=tuple_of_room[1]))
        return rooms_list

    def from_tuples_to_rooms_with_counter(self, tuple_of_rooms: list) -> list:
        rooms_list = []
        for tuple_of_room in tuple_of_rooms:
            room = dict()
            room["room"] = rooms.Room(id=tuple_of_room[0],
                                      name=tuple_of_room[1])
            room["counter"] = tuple_of_room[2]
            rooms_list.append(room)
        return rooms_list

    def from_namedtuple_to_dict(self, namedtuple_):
        return namedtuple_._asdict()

    def from_namedtuples_to_dicts(self, namedtuples):
        dicts = []
        for namedtuple_ in namedtuples:
            dicts.append(self.from_namedtuple_to_dict(namedtuple_))
        return dicts

    def from_namedtuples_to_dicts_with_counter(self, namedtuples):
        dicts = []
        for namedtuple_ in namedtuples:
            dict_ = self.from_namedtuple_to_dict(namedtuple_["room"])
            dict_["number_of_students"] = namedtuple_["counter"]
            dicts.append(dict_)
        return dicts
