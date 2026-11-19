import unittest
from datetime import date

from devolucao_atraso import atualizar_atraso, registrar_devolucao
from modelo import Emprestimo, Item


class TestAtraso(unittest.TestCase):
    def setUp(self):
        self.emprestimo = Emprestimo(Item("Projetor"), date(2026, 11, 10), date(2026, 11, 15))

    def test_marca_aberto_com_prazo_vencido(self):
        self.assertTrue(atualizar_atraso(self.emprestimo, date(2026, 11, 16)))
        self.assertEqual(self.emprestimo.situacao, "Em atraso")
        self.assertEqual(self.emprestimo.item.situacao, "Emprestado")

    def test_data_limite_ainda_esta_no_prazo(self):
        self.assertFalse(atualizar_atraso(self.emprestimo, date(2026, 11, 15)))
        self.assertEqual(self.emprestimo.situacao, "Ativo")

    def test_devolvido_permanece_devolvido_apos_prazo(self):
        registrar_devolucao(self.emprestimo, date(2026, 11, 14))
        self.assertFalse(atualizar_atraso(self.emprestimo, date(2026, 11, 16)))
        self.assertEqual(self.emprestimo.situacao, "Devolvido")
