from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional


@dataclass
class Usuario:
    id: int
    nome: str


@dataclass
class Item:
    id: int
    nome: str
    status: str = "Disponível"


@dataclass
class Emprestimo:
    id: int
    usuario: Usuario
    item: Item
    data_retirada: date
    data_prevista_devolucao: date
    situacao: str = "Ativo"
    historico_renovacoes: List[date] = field(default_factory=list)


class EmprestimoService:

    def renovar_prazo(self, emprestimo: Emprestimo, dias: int) -> date:

        if emprestimo.situacao != "Ativo":
            raise ValueError(
                "Não é possível renovar um empréstimo que não está ativo."
            )

        if dias <= 0:
            raise ValueError(
                "A quantidade de dias deve ser maior que zero."
            )

        nova_data = emprestimo.data_prevista_devolucao + timedelta(days=dias)

        emprestimo.data_prevista_devolucao = nova_data
        emprestimo.historico_renovacoes.append(nova_data)

        return nova_data

    def consultar_historico(
        self,
        emprestimos: List[Emprestimo],
        usuario_id: Optional[int] = None,
        item_id: Optional[int] = None
    ) -> List[Emprestimo]:

        resultado = emprestimos

        if usuario_id is not None:
            resultado = [
                e for e in resultado
                if e.usuario.id == usuario_id
            ]

        if item_id is not None:
            resultado = [
                e for e in resultado
                if e.item.id == item_id
            ]

        return list(resultado)