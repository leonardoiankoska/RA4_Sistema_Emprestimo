# language: pt
Funcionalidade: Devolução e atraso de empréstimos

  Contexto:
    Dado um projetor emprestado com retirada em "2026-11-10" e prazo em "2026-11-15"

  Cenário: Registrar devolução dentro do prazo
    Quando registro a devolução em "2026-11-14"
    Então o empréstimo fica "Devolvido"
    E o item fica "Disponível"
    E a data de devolução fica "2026-11-14"

  Cenário: Identificar um empréstimo em atraso
    Quando verifico o prazo em "2026-11-16"
    Então o empréstimo fica "Em atraso"
    E o item fica "Emprestado"

  Cenário: Consultar na data limite
    Quando verifico o prazo em "2026-11-15"
    Então o empréstimo fica "Ativo"
    E o item fica "Emprestado"

  Cenário: Consultar depois do prazo com item já devolvido
    Dado que registrei a devolução em "2026-11-14"
    Quando verifico o prazo em "2026-11-16"
    Então o empréstimo fica "Devolvido"
    E o item fica "Disponível"

  Cenário: Rejeitar segunda devolução
    Dado que registrei a devolução em "2026-11-14"
    Quando tento devolver novamente em "2026-11-15"
    Então recebo a mensagem "Empréstimo já devolvido."
    E a data de devolução fica "2026-11-14"
