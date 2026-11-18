from cadastro_itens import CadastroItens

def main():
    cadastro = CadastroItens()
    while True:
        print("\n1 - Cadastrar | 2 - Consultar | 3 - Listar | 0 - Sair")
        opcao = input("Opção: ")
        try:
            if opcao == "1":
                print(cadastro.cadastrar(input("Nome: "), input("Descrição: ")))
            elif opcao == "2":
                print(cadastro.consultar(int(input("ID: "))) or "Item não encontrado")
            elif opcao == "3":
                for item in cadastro.listar():
                    print(item)
            elif opcao == "0":
                break
            else:
                print("Opção inválida")
        except ValueError as erro:
            print(erro)

if __name__ == "__main__":
    main()
