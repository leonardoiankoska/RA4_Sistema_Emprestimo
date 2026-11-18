from item import Item

class CadastroItens:
    def __init__(self):
        self.itens = []
    def cadastrar(self, nome, descricao=""):
        raise NotImplementedError

    def consultar(self, id_item):
        raise NotImplementedError

    def listar(self):
        raise NotImplementedError
