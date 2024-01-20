'''8. Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.'''

valorHora = float(input("Digite o valor que você ganha por hora: "))
quantidadeHora = float(input("Digite a quantidade de horas trabalhas: "))

salarioMensal = valorHora * quantidadeHora

print(f'Salario mensal: {salarioMensal:.2f}')