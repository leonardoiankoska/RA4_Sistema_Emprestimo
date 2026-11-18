import pytest
from cadastro_itens import CadastroItens

def test_cadastro_valido():
    cadastro = CadastroItens()
    item = cadastro.cadastrar("Livro", "Literatura")
    assert (item.id, item.nome, item.descricao, item.status) == (1, "Livro", "Literatura", "Disponível")

@pytest.mark.parametrize("nome", ["", "   "])
def test_nome_obrigatorio(nome):
    with pytest.raises(ValueError, match="Nome obrigatório"):
        CadastroItens().cadastrar(nome)

def test_consulta_existente():
    cadastro = CadastroItens()
    item = cadastro.cadastrar("Livro")
    assert cadastro.consultar(item.id) == item

def test_consulta_inexistente():
    assert CadastroItens().consultar(999) is None

def test_listagem():
    cadastro = CadastroItens()
    a = cadastro.cadastrar("Livro")
    b = cadastro.cadastrar("Notebook")
    assert cadastro.listar() == [a, b]
    assert a.id != b.id
