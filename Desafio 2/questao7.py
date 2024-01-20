'''7. Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.'''

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 10:
    print("Usuário é uma criança")

elif idade > 10 and idade <= 18:
    print("Usuário é um adolescente")

elif idade > 18 and idade < 60:
    print("Usuario é um adulto")

else:
    print("Usuário é um idoso")