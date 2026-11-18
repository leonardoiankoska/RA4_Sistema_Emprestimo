from item import Item

class CadastroItens:
    def __init__(self):
        self.itens = []
    def cadastrar(self, nome, descricao=""):
        if not nome or not nome.strip():
            raise ValueError("Nome obrigatório")
        item = Item(len(self.itens)+1, nome.strip(), descricao)
        self.itens.append(item)
        return item

    def consultar(self, id_item):
        return next((item for item in self.itens if item.id == id_item), None)

    def listar(self):
        return self.itens.copy()
