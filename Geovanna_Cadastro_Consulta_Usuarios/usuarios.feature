# language: pt

Funcionalidade: Cadastro e consulta de usuários
  Como responsável pelo sistema de empréstimo de itens
  Quero cadastrar e consultar usuários
  Para identificar corretamente as pessoas que realizam empréstimos


  Cenário: Cadastrar usuário com dados válidos
    Dado que o usuário ainda não está cadastrado
    Quando informar o nome "Geovanna" e o e-mail "geo@gmail.com"
    Então o sistema deve cadastrar o usuário com sucesso


  Cenário: Impedir cadastro de usuário sem nome
    Dado que estou realizando o cadastro de um usuário
    Quando deixar o campo nome vazio
    Então o sistema deve impedir o cadastro
    E informar que o nome é obrigatório

  Cenário: Impedir cadastro de usuário sem e-mail
    Dado que está sendo realizado o cadastro de um novo usuário
    Quando o campo e-mail for deixado vazio
    Então o sistema deve impedir o cadastro
    E informar que o e-mail é obrigatório


  Cenário: Impedir cadastro com e-mail já utilizado
    Dado que existe um usuário cadastrado com o e-mail "geo@gmail.com"
    Quando tentar cadastrar outro usuário com o mesmo e-mail
    Então o sistema deve impedir o novo cadastro
    E informar que o e-mail já está cadastrado


  Cenário: Buscar usuário existente
    Dado que existe um usuário cadastrado com o e-mail "geo@gmail.com"
    Quando realizar uma busca pelo e-mail "geo@gmail.com"
    Então o sistema deve retornar os dados de Geovanna


  Cenário: Buscar usuário inexistente
    Dado que não existe usuário com o e-mail "naoexiste@gmail.com"
    Quando realizar uma busca pelo e-mail informado
    Então o sistema não deve retornar nenhum usuário


  Cenário: Listar usuários cadastrados
    Dado que existem usuários cadastrados no sistema
    Quando solicitar a listagem de usuários
    Então o sistema deve apresentar todos os usuários cadastrados