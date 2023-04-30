from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    nome_da_empresa = "Empresa"
    nome_do_produto = "produto"
    data_de_fabricacao = "31102000"
    data_de_validade = "31102100"
    numero_de_serie = "1A2B3C"
    instrucoes_de_armazenamento = "tutorial básico"

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert product.id == id
    assert product.nome_da_empresa == nome_da_empresa
    assert product.nome_do_produto == nome_do_produto
    assert product.data_de_fabricacao == data_de_fabricacao
    assert product.data_de_validade == data_de_validade
    assert product.numero_de_serie == numero_de_serie
    assert product.instrucoes_de_armazenamento == instrucoes_de_armazenamento
