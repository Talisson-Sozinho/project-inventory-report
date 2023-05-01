from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    products_mock = [
        {
            "id": "1",
            "nome_do_produto": "PRODUTO",
            "nome_da_empresa": "EMPRESA",
            "data_de_fabricacao": "2000-10-31",
            "data_de_validade": "2100-10-31",
            "numero_de_serie": "1A2B3C",
            "instrucoes_de_armazenamento": "tutorial básico",
        },
        {
            "id": "2",
            "nome_do_produto": "OUTRO PRODUTO",
            "nome_da_empresa": "EMPRESA",
            "data_de_fabricacao": "2004-08-04",
            "data_de_validade": "2104-08-04",
            "numero_de_serie": "123456",
            "instrucoes_de_armazenamento": "tutorial meio avançado",
        },
    ]

    result = ColoredReport(SimpleReport).generate(products_mock)

    except_result = (
        "\033[32mData de fabricação mais antiga:\033[0m"
        " \033[36m2000-10-31\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m"
        " \033[36m2100-10-31\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m \033[31mEMPRESA\033[0m"
    )
    assert result == except_result
