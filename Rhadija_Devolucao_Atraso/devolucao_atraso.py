from datetime import date

from modelo import Emprestimo

DEVOLVIDO = "Devolvido"
DISPONIVEL = "Disponível"
EM_ATRASO = "Em atraso"


def registrar_devolucao(emprestimo: Emprestimo, data: date) -> None:
    if emprestimo.devolvido_em is not None:
        raise ValueError("Empréstimo já devolvido.")
    if data < emprestimo.retirada:
        raise ValueError("Devolução anterior à retirada.")

    emprestimo.devolvido_em = data
    emprestimo.situacao = DEVOLVIDO
    emprestimo.item.situacao = DISPONIVEL


def atualizar_atraso(emprestimo: Emprestimo, hoje: date) -> bool:
    em_atraso = emprestimo.devolvido_em is None and hoje > emprestimo.prazo
    if em_atraso:
        emprestimo.situacao = EM_ATRASO
    return em_atraso
