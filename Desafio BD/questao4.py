'''4.Atualização e Remoção 
    a)Atualize a idade de um aluno específico natabela. 
    b)Remova um aluno pelo seu ID.'''

import sqlite3

conexao = sqlite3.connect('bd-python')
cursor = conexao.cursor()

dados = cursor.execute('UPDATE alunos SET idade=50 WHERE nome="Marina"')

dados = cursor.execute('DELETE FROM alunos WHERE id=2')

for usuario in dados:
     print(usuario)


conexao.commit()
conexao.close