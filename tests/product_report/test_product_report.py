from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_do_produto = "PRODUTO"
    nome_da_empresa = "EMPRESA"
    data_de_fabricacao = "31102000"
    data_de_validade = "31102100"
    numero_de_serie = "1A2B3C"
    instrucoes_de_armazenamento = "tutorial basico de produto"
    data_de_fabricacao = "31102000"

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento
    )

    expect_text = (
        f"O produto {nome_do_produto}"
        f" fabricado em {data_de_fabricacao}"
        f" por {nome_da_empresa} com validade"
        f" até {data_de_validade}"
        f" precisa ser armazenado {instrucoes_de_armazenamento}."
    )

    assert str(product.__repr__()) == expect_text
