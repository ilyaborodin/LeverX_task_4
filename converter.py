class Converter:
    def from_tuples_to_dicts(self, tuple_of_rooms: list) -> list:
        rooms_list = []
        for tuple_of_room in tuple_of_rooms:
            room = {
                "id": tuple_of_room[0],
                "name": tuple_of_room[1]
            }
            rooms_list.append(room)
        return rooms_list

    def from_tuples_to_dicts_with_counter(self, tuple_of_rooms: list) -> list:
        rooms_list = []
        for tuple_of_room in tuple_of_rooms:
            room = {
                "id": tuple_of_room[0],
                "name": tuple_of_room[1],
                "counter": tuple_of_room[2]
            }
            rooms_list.append(room)
        return rooms_list
