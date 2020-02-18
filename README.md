Added docker-compose

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
