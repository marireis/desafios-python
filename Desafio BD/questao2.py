'''2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.'''

import sqlite3

conexao = sqlite3.connect('bd-python')
cursor = conexao.cursor()

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Marina", 30, "Nutrição")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Lily", 29, "Arquitetura")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Joao", 31, "Computação")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Fernanda", 33, "Nutrição")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Kaio", 25, "Direito")')

conexao.commit()
conexao.close