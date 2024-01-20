'''9. Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.'''

horasExercicio = float(input("Quantidade horas de exercício por semana: "))

horasEmMinutos = horasExercicio*60
print(horasEmMinutos, 'minutos')

caloriasQueimadas = horasEmMinutos * 5

print(f'Quantidade de calorias perdidas: {caloriasQueimadas}')
