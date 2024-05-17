# USANDO O 'ELIF' SERIA O MESMO DE UM ELSE IF    
saldo = 2000
opcao = int(input("Digite o número da operação: [1] - SAQUE | [2] - SALDO: "))

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