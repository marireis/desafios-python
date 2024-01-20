'''2. Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = input("Informe qual letra se refere ao turno que você estuda (M-matutino, V-vespertino, N- noturno)")

if turno == 'M' or 'm':
    print('Bom dia!')
elif turno ==  'V' or 'v':
    print('Boa tarde!')
elif turno == 'N' or 'n':
    print('Boa noite')
else:
    print('Valor Inválido')