'''7. Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).'''

peso = float(input("Digite o seu peso(kg): "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura*altura)

print(f'Seu IMC eh:{imc:.2f}')