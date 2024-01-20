#1. Faça um Programa que peça dois números, realize as principais
#operações soma, subtração, multiplicação, divisão

numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 2: '))


soma = numero1 + numero2
print('Soma: ', soma)

if(numero1>numero2):
    subtracao = numero1 - numero2
    print('Subtração: ',subtracao)
else:
    print('Não é possível realizar a subtração, número 1 < número 2')

multiplicacao = numero1 * numero2
print('Multiplicação: ', multiplicacao)

if(numero1 < numero2):
    divisao = numero1/numero2
    print('Divisão: ', divisao)
    
else:
    print('Não é possível realizar a divisão, número 1 < número 2')






