import unittest
from datetime import date

from emprestimo_service import (
    Usuario,
    Item,
    Emprestimo,
    EmprestimoService
)


class TestRenovacaoEHistorico(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario(1, "Ana")
        self.item = Item(10, "Livro")

        self.emprestimo = Emprestimo(
            id=100,
            usuario=self.usuario,
            item=self.item,
            data_retirada=date(2026, 11, 1),
            data_prevista_devolucao=date(2026, 11, 10)
        )

        self.service = EmprestimoService()

    def test_renovar_prazo_acrescenta_dias(self):

        nova_data = self.service.renovar_prazo(
            self.emprestimo, 7
        )

        self.assertEqual(nova_data, date(2026, 11, 17))

        self.assertEqual(
            self.emprestimo.data_prevista_devolucao,
            date(2026, 11, 17)
        )

    def test_renovar_prazo_invalido(self):

        with self.assertRaises(ValueError):
            self.service.renovar_prazo(
                self.emprestimo, 0
            )

    def test_nao_renovar_emprestimo_encerrado(self):

        self.emprestimo.situacao = "Devolvido"

        with self.assertRaises(ValueError):
            self.service.renovar_prazo(
                self.emprestimo, 5
            )

    def test_historico_por_usuario(self):

        outro_usuario = Usuario(2, "Bruno")
        outro_item = Item(11, "Caderno")

        outro_emprestimo = Emprestimo(
            id=101,
            usuario=outro_usuario,
            item=outro_item,
            data_retirada=date(2026, 11, 2),
            data_prevista_devolucao=date(2026, 11, 12)
        )

        resultado = self.service.consultar_historico(
            [self.emprestimo, outro_emprestimo],
            usuario_id=1
        )

        self.assertEqual(
            [e.id for e in resultado],
            [100]
        )

    def test_historico_por_item(self):

        resultado = self.service.consultar_historico(
            [self.emprestimo],
            item_id=10
        )

        self.assertEqual(len(resultado), 1)

        self.assertEqual(
            resultado[0].item.nome,
            "Livro"
        )


if __name__ == "__main__":
    unittest.main()