# USANDO AS CONDICIONAIS 'IF' E 'ELSE'
saldo = 1500
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    saldo -= saque
    print(f" Saque realizado com Sucesso, seu saldo atual é de : R$:{saldo}")

else:
    print("Saldo insuficiente!")    



