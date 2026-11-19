# language: pt

Funcionalidade: Renovação de prazo e consulta de histórico de empréstimos
  Como responsável pelo sistema de empréstimo de itens
  Quero renovar o prazo de empréstimos ativos e consultar o histórico por usuário ou item
  Para manter o controle atualizado dos prazos e o rastreamento dos registros

  Cenário: Renovar prazo de um empréstimo ativo com sucesso
    Dado que existe um empréstimo ativo para o usuário "Ana" com o item "Livro"
    E a data prevista de devolução é "2026-11-10"
    Quando for solicitada a renovação do prazo por 7 dias
    Então o sistema deve atualizar a data prevista de devolução para "2026-11-17"
    E registrar a nova data no histórico de renovações do empréstimo

  Cenário: Impedir renovação com quantidade de dias inválida
    Dado que existe um empréstimo ativo no sistema
    Quando for solicitada a renovação do prazo com 0 dias
    Então o sistema deve impedir a renovação
    E informar que a quantidade de dias deve ser maior que zero

  Cenário: Impedir renovação de empréstimo já encerrado
    Dado que existe um empréstimo com situação "Devolvido"
    Quando for solicitada a renovação do prazo por 5 dias
    Então o sistema deve impedir a renovação
    E informar que não é possível renovar um empréstimo que não está ativo

  Cenário: Consultar histórico de empréstimos por usuário
    Dado que existem empréstimos registrados para os usuários "Ana" e "Bruno"
    Quando for realizada uma consulta de histórico filtrando pelo usuário "Ana"
    Então o sistema deve retornar apenas os empréstimos vinculados à usuária "Ana"

  Cenário: Consultar histórico de empréstimos por item
    Dado que existem empréstimos registrados no sistema para o item "Livro"
    Quando for realizada uma consulta de histórico filtrando pelo item "Livro"
    Então o sistema deve retornar os registros correspondentes ao item "Livro"