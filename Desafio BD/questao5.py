'''5.Criar uma Tabela e Inserir Dados 
    Crie uma tabela chamada "clientes" com os campos: 
    id (chave primária),nome(texto), idade(inteiro)e saldo(float).
    Insira alguns registros de clientes na tabela.'''


import sqlite3

conexao = sqlite3.connect('bd-python')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo NUMERIC );')

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Marina", 40, 500.05)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Francisco", 20, 1500.05)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Joao", 30, 300.05)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Lua", 60, 400.05)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Bruna", 70, 2500.05)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (6, "Mateus", 20, 3500.05)')


conexao.commit()
conexao.close