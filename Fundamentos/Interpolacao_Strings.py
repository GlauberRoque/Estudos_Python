#INTERPOLAÇÃO DE STRINGS

nome = "Glauber"
idade = 34
profissao = "Desenvolvedor"

#MODO OLD
print("Oi, me chamo %s. Tenho %d anos de idade e sou %s." %(nome, idade, profissao))

#METODO .FORMAT
print("Oi, me chamo {}. Tenho {} anos de idade e sou {}." .format(nome, idade, profissao))

print("Oi, me chamo {2}. Tenho {0} anos de idade e sou {1}." .format(idade, profissao, nome))

#METODO F-STRING
print(f"Oi, me chamo {nome}. Tenho {idade} anos de idade e sou {profissao}.")

# F-STRING PARA FORMATAR VALORES
pi = 3.14159

print(f"O valor de PI é: {pi:.2f}")