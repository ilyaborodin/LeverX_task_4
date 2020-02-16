Создал сущности student и room для передачи информации между классами. Информацию вводил через них. Но выводил через словари,
так как в этом задании(не требуется проводить дополнительные действия над обьектами) это усложнит логику и количество операций.
Добавил docker-compose c уже подключенной бд к программе. 

To run database: sudo docker-compose up --build

Help:
usage: main.py [-h] path_to_students path_to_rooms {json,xml}

Command-line utility.

positional arguments:
  path_to_students  Path to students file
  path_to_rooms     Path to rooms file
  {json,xml}        Output format

optional arguments:
  -h, --help        show this help message and exit
