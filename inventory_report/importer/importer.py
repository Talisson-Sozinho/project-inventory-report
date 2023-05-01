from abc import ABC, abstractclassmethod


class Importer(ABC):
    @abstractclassmethod
    def import_data(cls, path: str) -> list[dict]:
        raise NotImplementedError
