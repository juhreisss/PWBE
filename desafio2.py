def simular_banco():
    saldo = 0

    while True:
        print("\n1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print("4 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))
            saldo += valor
            print("Saldo:", saldo)

        elif opcao == "2":
            valor = float(input("Digite o valor do saque: "))
            if valor <= saldo:
                saldo -= valor
                print("Saldo:", saldo)
            else:
                print("Saldo insuficiente")

        elif opcao == "3":
            print("Saldo:", saldo)

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida")

simular_banco()
