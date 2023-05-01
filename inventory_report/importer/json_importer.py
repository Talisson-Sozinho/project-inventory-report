from inventory_report.importer.importer import Importer
from json import load
import os


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list[dict]:
        if os.path.splitext(path)[1] != ".json":
            raise ValueError("Arquivo inválido")

        return cls.read_file(path)

    @staticmethod
    def read_file(path: str) -> list[dict]:
        with open(path) as file:
            return load(file)
