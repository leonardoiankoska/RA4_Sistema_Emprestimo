import unittest
from usuario import UsuarioService


class TestUsuarioService(unittest.TestCase):

    def setUp(self):
        self.service = UsuarioService()

    def test_cadastrar_usuario_com_dados_validos(self):
        usuario = self.service.cadastrar_usuario(
            "Geovanna",
            "geo@gmail.com"
        )

        self.assertEqual(usuario["nome"], "Geovanna")
        self.assertEqual(usuario["email"], "geo@gmail.com")
        self.assertEqual(usuario["id"], 1)

    def test_nao_cadastrar_usuario_sem_nome(self):
        with self.assertRaisesRegex(
            ValueError,
            "Nome é obrigatório"
        ):
            self.service.cadastrar_usuario(
                "",
                "geo@gmail.com"
            )

    def test_nao_cadastrar_usuario_sem_email(self):
        with self.assertRaisesRegex(
            ValueError,
            "E-mail é obrigatório"
        ):
            self.service.cadastrar_usuario(
                "Geovanna",
                ""
            )

    def test_nao_cadastrar_email_duplicado(self):
        self.service.cadastrar_usuario(
            "Geovanna",
            "geo@gmail.com"
        )

        with self.assertRaisesRegex(
            ValueError,
            "E-mail já cadastrado"
        ):
            self.service.cadastrar_usuario(
                "Outra Pessoa",
                "geo@gmail.com"
            )

    def test_buscar_usuario_existente(self):
        self.service.cadastrar_usuario(
            "Geovanna",
            "geo@gmail.com"
        )

        usuario = self.service.buscar_usuario_por_email(
            "geo@gmail.com"
        )

        self.assertIsNotNone(usuario)
        self.assertEqual(usuario["nome"], "Geovanna")

    def test_buscar_usuario_inexistente(self):
        usuario = self.service.buscar_usuario_por_email(
            "naoexiste@gmail.com"
        )

        self.assertIsNone(usuario)

    def test_listar_usuarios(self):
        self.service.cadastrar_usuario(
            "Geovanna",
            "geo@gmail.com"
        )

        self.service.cadastrar_usuario(
            "Maria",
            "maria@gmail.com"
        )

        usuarios = self.service.listar_usuarios()

        self.assertEqual(len(usuarios), 2)

if __name__ == "__main__":
    unittest.main()