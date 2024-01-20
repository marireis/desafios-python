'''1. Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"".'''

resposta = []

resposta.append(input("Telefonou para a vítima? S-1/ 0-N: "))
resposta.append(input("Esteve no local do crime? S-1/ 0-N: "))
resposta.append(input("Mora perto da vítima?  S-1/ 0-N: "))
resposta.append(input("Devia para a vítima?  S-1/ 0-N: "))
resposta.append(input("Já trabalhou com a vítima?  S-1/ 0-N: "))

somaResp = 0 

for i in resposta:  
    somaResp += int(i) 
    
if (somaResp < 2): 
    print("\nInocente") 
elif (somaResp == 2):
    print("\nSuspeita") 
elif (3 <= somaResp <= 4):
    print("\nCúmplice") 
elif (somaResp == 5):
    print("\nAssassino")
