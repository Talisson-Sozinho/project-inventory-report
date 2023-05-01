from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data: list[dict]) -> str:
        simple_report = super().generate(data)
        quantity_of_products_per_company = cls.get_products_per_company(data)
        complete_report = ""
        for company, quantity in quantity_of_products_per_company.items():
            complete_report += f" - {company}: {quantity}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{complete_report}"
        )
