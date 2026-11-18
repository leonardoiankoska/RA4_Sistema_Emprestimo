class UsuarioService:

    def __init__(self):
        self.usuarios = []
        self.proximo_id = 1

    def cadastrar_usuario(self, nome, email):

        nome = nome.strip()
        email = email.strip()

        if not nome:
            raise ValueError("Nome é obrigatório")

        if not email:
            raise ValueError("E-mail é obrigatório")

        for usuario in self.usuarios:
            if usuario["email"].lower() == email.lower():
                raise ValueError("E-mail já cadastrado")

        usuario = {
            "id": self.proximo_id,
            "nome": nome,
            "email": email
        }

        self.usuarios.append(usuario)
        self.proximo_id += 1

        return usuario

    def buscar_usuario_por_email(self, email):

        email = email.strip().lower()

        for usuario in self.usuarios:
            if usuario["email"].lower() == email:
                return usuario

        return None

    def listar_usuarios(self):
        return self.usuarios.copy()