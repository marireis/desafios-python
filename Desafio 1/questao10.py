'''10. Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.'''

saudacao = input('Oi, tudo bem!')
nome = input('Eu me chamo Marina, tenho 31 anos')
emprego = input('Atualmente trabalho como desenvolvedora back-end')

concatenaString = saudacao + '' + nome + '' + emprego 
print(concatenaString)