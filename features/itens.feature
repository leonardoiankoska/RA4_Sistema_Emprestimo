# language: pt
Funcionalidade: Cadastro e consulta de itens
  Cenário: Cadastro válido
    Dado um cadastro vazio
    Quando cadastro o item "Livro"
    Então o item deve estar disponível

  Cenário: Cadastro sem nome
    Dado um cadastro vazio
    Quando tento cadastrar um item sem nome
    Então o cadastro deve ser rejeitado

  Cenário: Consulta existente
    Dado um cadastro com um livro
    Quando consulto o item 1
    Então encontro o livro

  Cenário: Consulta inexistente
    Dado um cadastro vazio
    Quando consulto o item 999
    Então nenhum item é encontrado

  Cenário: Listagem
    Dado um cadastro com um livro
    Quando listo os itens
    Então a lista contém o livro
