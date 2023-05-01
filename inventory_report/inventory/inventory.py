from inventory_report.reports.complete_report import (
    CompleteReport,
    SimpleReport,
)
from csv import DictReader
from json import load
import xml.etree.ElementTree as ET
import os


class Inventory:
    @classmethod
    def import_data(cls, path: str, type_of_report: str):
        file_format = os.path.splitext(path)[1]

        if file_format == ".csv":
            data = cls.read_csv_file(path)

        if file_format == ".json":
            data = cls.read_json_file(path)

        if file_format == ".xml":
            data = cls.read_xml_file(path)

        if type_of_report == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)

    @staticmethod
    def read_csv_file(path: str) -> list[dict]:
        with open(path) as file:
            csv_iterable = DictReader(file)
            file_converted = [row for row in csv_iterable]
            return file_converted

    @staticmethod
    def read_json_file(path: str) -> list[dict]:
        with open(path) as file:
            return load(file)

    @staticmethod
    def read_xml_file(path: str) -> list[dict]:
        with open(path) as file:
            tree_xml = ET.parse(file)
            root_xml = tree_xml.getroot()

            return [
                {product.tag: product.text for product in record}
                for record in root_xml
            ]
