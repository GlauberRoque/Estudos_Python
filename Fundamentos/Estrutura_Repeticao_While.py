saldo = 5000

while opcao != 0:
    opcao = int(input("Digite o número da operação: [1] - SAQUE \n[2] - SALDO \n[0] - SAIR \n: "))

    if opcao == 1:
        saque = float(input("Informe o valor que deseja sacar: "))

        if saldo >= saque:
            saldo -= saque
            print(f" Saque realizado com Sucesso, seu saldo atual é de : R$:{saldo}")
        else:
            print("Saldo insuficiente!")

    elif opcao == 2:
        print("Imprimindo Extrato...")
        print(f"Seu saldo atual é de: {saldo}")

    else:
        sys.exit("Opção inválida!")  

