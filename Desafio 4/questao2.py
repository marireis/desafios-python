'''2. Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.'''

def reverso(num):
    return str(num[::-1])

num = str(input('Digite um número: ')).strip()
print(f'Reverso: {reverso(num)}')