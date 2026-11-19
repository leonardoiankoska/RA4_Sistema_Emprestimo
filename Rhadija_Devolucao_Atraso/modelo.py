from dataclasses import dataclass
from datetime import date


@dataclass
class Item:
    nome: str
    situacao: str = "Emprestado"


@dataclass
class Emprestimo:
    item: Item
    retirada: date
    prazo: date
    situacao: str = "Ativo"
    devolvido_em: date | None = None
