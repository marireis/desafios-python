'''5. Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.'''


def contar_vogais():
    i = 0
    j = 0
    string = str (input("Digite uma frase: "))
    for i in string:
        if (i == 'A' or i == 'a'
        or i == 'E' or i == 'e'
        or i == 'I' or i == 'i'
        or i == 'O' or i == 'o'
        or i == 'U' or i == 'u'):
             j+=1
    print("vogais: ", j)

contar_vogais()