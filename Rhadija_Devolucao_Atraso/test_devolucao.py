import unittest
from datetime import date

from devolucao_atraso import registrar_devolucao
from modelo import Emprestimo, Item


class TestDevolucao(unittest.TestCase):
    def setUp(self):
        self.emprestimo = Emprestimo(Item("Projetor"), date(2026, 11, 10), date(2026, 11, 15))

    def test_registra_data_e_libera_item(self):
        data = date(2026, 11, 14)
        registrar_devolucao(self.emprestimo, data)
        self.assertEqual(self.emprestimo.devolvido_em, data)
        self.assertEqual(self.emprestimo.situacao, "Devolvido")
        self.assertEqual(self.emprestimo.item.situacao, "Disponível")

    def test_devolucao_apos_o_prazo_libera_item(self):
        self.emprestimo.situacao = "Em atraso"
        registrar_devolucao(self.emprestimo, date(2026, 11, 16))
        self.assertEqual(self.emprestimo.situacao, "Devolvido")
        self.assertEqual(self.emprestimo.item.situacao, "Disponível")

    def test_rejeita_devolucao_repetida(self):
        data = date(2026, 11, 14)
        registrar_devolucao(self.emprestimo, data)
        with self.assertRaisesRegex(ValueError, "já devolvido"):
            registrar_devolucao(self.emprestimo, date(2026, 11, 15))
        self.assertEqual(self.emprestimo.devolvido_em, data)

    def test_rejeita_data_anterior_a_retirada(self):
        with self.assertRaisesRegex(ValueError, "anterior à retirada"):
            registrar_devolucao(self.emprestimo, date(2026, 11, 9))
        self.assertIsNone(self.emprestimo.devolvido_em)
        self.assertEqual(self.emprestimo.item.situacao, "Emprestado")
