import sys
import os
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor

READER_MAP = {
    ".csv": CsvImporter,
    ".json": JsonImporter,
    ".xml": XmlImporter,
}


def main():
    try:
        _, path, type_of_report = sys.argv
    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
        return

    file_format = os.path.splitext(path)[1]

    inventory = InventoryRefactor(READER_MAP[file_format])

    data = inventory.import_data(path, type_of_report)

    print(data, end="")


if __name__ == "__main__":
    main()
