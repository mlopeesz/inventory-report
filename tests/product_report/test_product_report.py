from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        "Gelobol",
        "AloAmbev",
        "10-05-2022",
        "10-05-2025",
        "A1B2C3D4E5",
        "Com pressão",
    )

    result = (
        f"O produto {produto.nome_do_produto}"
        f" fabricado em {produto.data_de_fabricacao}"
        f" por {produto.nome_da_empresa} com validade"
        f" até {produto.data_de_validade}"
        f" precisa ser armazenado {produto.instrucoes_de_armazenamento}."
    )

    assert produto.__repr__() == result
