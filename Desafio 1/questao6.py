'''6. Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''

distanciaViagem = float(input("Digite a distancia da viagem: "))

viagemAviao = distanciaViagem / 600
viagemCarro = distanciaViagem / 100
viagemOnibus = distanciaViagem / 80

print(f'Viagem de avião leva:{viagemAviao:.2f}h')

print(f'Viagem de avião leva:{viagemCarro:.2f}h')

print(f'Viagem de avião leva:{viagemOnibus:.2f}h')
