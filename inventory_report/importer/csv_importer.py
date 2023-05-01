from inventory_report.importer.importer import Importer
from csv import DictReader
import os


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list[dict]:
        if os.path.splitext(path)[1] != ".csv":
            raise ValueError("Arquivo inválido")

        return cls.read_file(path)

    @staticmethod
    def read_file(path: str) -> list[dict]:
        with open(path) as file:
            csv_iterable = DictReader(file)
            file_converted = [row for row in csv_iterable]
            return file_converted
