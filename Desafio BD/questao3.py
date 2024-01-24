'''3.Consultas Básicas 
Escreva consultas SQL para realizar as seguintes tarefas:
    a)Selecionar todos os registros da tabela "alunos".
    b)Selecionar o nome e a idade dos alunos com mais de 20 anos. 
    c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética. 
    d)Contar o número total de alunos na tabela'''

import sqlite3

conexao = sqlite3.connect('bd-python')
cursor = conexao.cursor()

dados = cursor.execute('SELECT * FROM alunos')
dados = cursor.execute('SELECT * FROM alunos WHERE idade>20')
dados = cursor.execute('SELECT curso FROM alunos GOURP BY nome ') 
dados = cursor.execute('SELECT COUNT(nome) FROM alunos') 
for usuario in dados:
     print(usuario)


conexao.commit()
conexao.close