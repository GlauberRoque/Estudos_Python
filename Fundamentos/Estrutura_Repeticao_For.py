# FOR
#texto = input("Digite seu nome: ")
texto = ""
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()    

for numero in range(0, 91, 9): #USANDO RANGE PARA SIMULAR UMA TABUADA
    print(numero, end=" ")