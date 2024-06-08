# código para execução do programa
from banco import Banco

def main():
    banco = Banco()

    while True:
        banco.menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            conta = banco.entrar()
            if conta:
                while True:
                    banco.menu_usuario()
                    opcao_usuario = input("Escolha uma opção: ")
                    if opcao_usuario == "1":
                        saldo, data_consulta = conta.consultar_saldo()
                        print(f"Seu saldo é R$ {saldo:.2f}. Consultado em: {data_consulta}")
                    elif opcao_usuario == "2":
                        valor = float(input("Digite o valor a depositar: ").replace(",", "."))
                        conta.depositar(valor)
                        print("Depósito realizado com sucesso!")
                    elif opcao_usuario == "3":
                        valor = float(input("Digite o valor a sacar: ").replace(",", "."))
                        if conta.sacar(valor):
                            print("Saque realizado com sucesso!")
                        else:
                            print("Saldo insuficiente!")
                    elif opcao_usuario == "4":
                        print("Saindo do programa...")
                        break
                    else:
                        print("Opção inválida!")

        elif opcao == "2":
            banco.cadastrar_usuario()
        elif opcao == "3":
            banco.deletar_usuario()
        elif opcao == "4":
            print("Obrigado por utilizar nosso Banco Python!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
