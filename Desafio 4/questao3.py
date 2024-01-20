'''3. Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.'''

def celsiusFahrenheit(celsius):
    fah = (celsius*9/5) + 32
    return fah

def fahrenheitCelsius(fah):
    celsius = (fah-32)*5/9
    return celsius


def menu():
    while True:
        opcao = int(input('Escolha: 1 para converter Celsius para Farenheit ou \n' +
                       '2 para converter Farenheit para Celsius: '))
        if opcao==1:
            celsius=int( input('Graus Celsius: ') )
            print('Convertido: ', celsiusFahrenheit(celsius),' graus Farenheit\n')
        elif opcao==2:
            fah=int( input('Graus Farenheit: ') )
            print('Convertido: ', fahrenheitCelsius(fah),' graus Celsius\n')
        else:
            print('Opção inválida')
            break

menu()