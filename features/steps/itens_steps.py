from behave import given, when, then
from cadastro_itens import CadastroItens

@given('um cadastro vazio')
def vazio(context):
    context.cadastro = CadastroItens()

@given('um cadastro com um livro')
def com_livro(context):
    context.cadastro = CadastroItens()
    context.livro = context.cadastro.cadastrar("Livro")

@when('cadastro o item "{nome}"')
def cadastrar(context, nome):
    context.item = context.cadastro.cadastrar(nome)

@then('o item deve estar disponível')
def disponivel(context):
    assert context.item.status == "Disponível"
    assert context.cadastro.consultar(context.item.id) == context.item

@when('tento cadastrar um item sem nome')
def invalido(context):
    context.erro = None
    try:
        context.cadastro.cadastrar("")
    except ValueError as erro:
        context.erro = str(erro)

@then('o cadastro deve ser rejeitado')
def rejeitado(context):
    assert context.erro == "Nome obrigatório"
    assert context.cadastro.listar() == []

@when('consulto o item {id_item:d}')
def consultar(context, id_item):
    context.resultado = context.cadastro.consultar(id_item)

@then('encontro o livro')
def encontrado(context):
    assert context.resultado == context.livro

@then('nenhum item é encontrado')
def inexistente(context):
    assert context.resultado is None

@when('listo os itens')
def listar(context):
    context.resultado = context.cadastro.listar()

@then('a lista contém o livro')
def lista(context):
    assert context.resultado == [context.livro]
