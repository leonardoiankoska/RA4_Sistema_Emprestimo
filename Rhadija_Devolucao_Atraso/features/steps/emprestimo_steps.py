from datetime import date

from behave import given, then, when

from devolucao_atraso import atualizar_atraso, registrar_devolucao
from modelo import Emprestimo, Item


@given('um projetor emprestado com retirada em "{retirada}" e prazo em "{prazo}"')
def criar_emprestimo(context, retirada, prazo):
    context.emprestimo = Emprestimo(Item("Projetor"), date.fromisoformat(retirada), date.fromisoformat(prazo))


@given('que registrei a devolução em "{dia}"')
@when('registro a devolução em "{dia}"')
def devolver(context, dia):
    registrar_devolucao(context.emprestimo, date.fromisoformat(dia))


@when('verifico o prazo em "{dia}"')
def consultar(context, dia):
    atualizar_atraso(context.emprestimo, date.fromisoformat(dia))


@when('tento devolver novamente em "{dia}"')
def tentar_devolver(context, dia):
    context.mensagem = None
    try:
        devolver(context, dia)
    except ValueError as erro:
        context.mensagem = str(erro)


@then('o empréstimo fica "{situacao}"')
def conferir_emprestimo(context, situacao):
    assert context.emprestimo.situacao == situacao, context.emprestimo.situacao


@then('o item fica "{situacao}"')
def conferir_item(context, situacao):
    assert context.emprestimo.item.situacao == situacao, context.emprestimo.item.situacao


@then('a data de devolução fica "{dia}"')
def conferir_data(context, dia):
    assert context.emprestimo.devolvido_em == date.fromisoformat(dia), context.emprestimo.devolvido_em


@then('recebo a mensagem "{mensagem}"')
def conferir_mensagem(context, mensagem):
    assert context.mensagem == mensagem, context.mensagem
