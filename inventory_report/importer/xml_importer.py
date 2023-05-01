from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET
import os


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list[dict]:
        if os.path.splitext(path)[1] != ".xml":
            raise ValueError("Arquivo inválido")

        return cls.read_file(path)

    @staticmethod
    def read_file(path: str) -> list[dict]:
        with open(path) as file:
            tree_xml = ET.parse(file)
            root_xml = tree_xml.getroot()

            return [
                {product.tag: product.text for product in record}
                for record in root_xml
            ]
