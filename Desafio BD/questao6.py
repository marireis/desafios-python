'''6.Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:
    a)Selecione o nome e a idade dos clientes com idade superior a 30 anos. 
    b)Calcule o saldo médio dos clientes.
    c)Encontre o cliente com o saldo máximo. 
    d)Conte quantos clientes têm saldo acima de 1000.'''

import sqlite3

conexao = sqlite3.connect('bd-python')
cursor = conexao.cursor()

dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')

for usuario in dados:
    print(usuario)

conexao.commit()
conexao.close