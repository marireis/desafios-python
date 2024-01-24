'''7.Atualização e Remoção com Condições 
    a)Atualize o saldo de um cliente específico. 
    b)Remova um cliente pelo seu ID.'''

import sqlite3

conexao = sqlite3.connect('bd-python')
cursor = conexao.cursor()

cursor.execute('UPDATE clientes SET nome="Matheus Lopes" WHERE nome = "Mateus"')
cursor.execute('DELETE FROM clientes WHERE nome="Lua"')

for usuario in dados:
    print(usuario)

conexao.commit()
conexao.close