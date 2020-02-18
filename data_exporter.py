import json
import dicttoxml
from xml.dom.minidom import parseString


class JsonExporter:
    """Класс преобразует наши данные в файлы json"""
    def export(self, data_to_export: list or dict, name_of_file: str) -> None:
        with open("{}.json".format(name_of_file), "w", encoding="utf-8") as file:
            json_text = json.dumps(data_to_export, indent=2)
            file.writelines(json_text)


class XmlExporter:
    """Класс преобразует наши данные в файлы xml"""
    def export(self, data_to_export: list or dict, name_of_file: str) -> None:
        xml = dicttoxml.dicttoxml(data_to_export)
        parsed_xml = parseString(xml)
        with open("{}.xml".format(name_of_file), "w", encoding="utf-8") as file:
            file.write(parsed_xml.toprettyxml())
