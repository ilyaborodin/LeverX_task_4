import json
import dicttoxml
from xml.dom.minidom import parseString


class DataExporter:
    """Класс преобразует наши данные в файлы json/xml"""
    def export_to(self, data_to_export: list or dict or tuple,
                  format_of_output: str, name_of_file: str) -> None:
        if format_of_output == "json":
            self._export_to_json(data_to_export, name_of_file)
        else:
            self._export_to_xml(data_to_export, name_of_file)

    def _export_to_json(self, data_to_export: list or dict, name_of_file: str) -> None:
        with open("{}.json".format(name_of_file), "w", encoding="utf-8") as file:
            json_text = json.dumps(data_to_export, indent=2)
            file.writelines(json_text)

    def _export_to_xml(self, data_to_export: list or dict, name_of_file: str) -> None:
        xml = dicttoxml.dicttoxml(data_to_export)
        parsed_xml = parseString(xml)
        with open("{}.xml".format(name_of_file), "w", encoding="utf-8") as file:
            file.write(parsed_xml.toprettyxml())
