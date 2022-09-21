from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        'Gelobol',
        'AloAmbev',
        '10-05-2022',
        '10-05-2025',
        'A1B2C3D4E5',
        'Com pressão',
    )

    assert produto.id == 1
    assert produto.nome_do_produto == 'Gelobol'
    assert produto.nome_da_empresa == 'AloAmbev'
    assert produto.data_de_fabricacao == '10-05-2022'
    assert produto.data_de_validade == '10-05-2025'
    assert produto.numero_de_serie == 'A1B2C3D4E5'
    assert produto.instrucoes_de_armazenamento == 'Com pressão'
