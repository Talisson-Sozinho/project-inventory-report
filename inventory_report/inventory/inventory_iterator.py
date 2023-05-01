from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data: list[dict]):
        self.data = data
        self.target = 0

    def __next__(self):
        data = self.data[self.target]

        if not data:
            raise StopIteration()

        self.target += 1
        return data
