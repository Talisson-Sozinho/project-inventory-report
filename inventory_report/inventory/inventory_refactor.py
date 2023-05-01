from inventory_report.reports.complete_report import (
    CompleteReport,
    SimpleReport,
)
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer) -> str:
        self.importer = importer
        self.data = []

    def import_data(self, path: str, type_of_report: str):
        self.load_data(path)
        if type_of_report == "simples":
            return SimpleReport.generate(self.data)
        return CompleteReport.generate(self.data)

    def load_data(self, path: str) -> None:
        self.data.extend(self.importer.import_data(path))

    def __iter__(self):
        return InventoryIterator(self.data)
