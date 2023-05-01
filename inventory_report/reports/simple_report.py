from datetime import date


class SimpleReport:
    @classmethod
    def generate(cls, data: list[dict]) -> str:
        earliest_date_manufacture = cls.get_min_date_manufacture(data)
        earliest_expiration_date = cls.get_min_expiration_date(data)
        company_with_more_products = cls.get_company_with_more_products(data)

        return f"""Data de fabricação mais antiga: {earliest_date_manufacture}
Data de validade mais próxima: {earliest_expiration_date}
Empresa com mais produtos: {company_with_more_products}
"""

    @staticmethod
    def get_min_date_manufacture(data: list[dict]) -> str:
        return min(data, key=lambda data: data["data_de_fabricacao"])[
            "data_de_fabricacao"
        ]

    @staticmethod
    def get_min_expiration_date(data: list[dict]) -> str:
        today = date.today()
        return min(
            [
                product["data_de_validade"]
                for product in data
                if date.fromisoformat(product["data_de_validade"]) > today
            ]
        )

    @staticmethod
    def get_company_with_more_products(data: list[dict]) -> str:
        count_company = {}
        for product in data:
            if product["nome_da_empresa"] in count_company:
                count_company[product["nome_da_empresa"]] += 1
            else:
                count_company[product["nome_da_empresa"]] = 1

        return max(count_company.items(), key=lambda company: company[1])[0]
