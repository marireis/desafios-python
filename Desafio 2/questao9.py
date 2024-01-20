'''9. O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.'''

n = 1 
par = 0 
impar = 0 

while True: 
    a = int(input("Digite um numero:"))
    if a == 0:
        break
    n = n + 1 
    if a % 2 == 0:
        a = par
        par = par + 1 
    else:  
        a = impar 
        impar = impar + 1  

print("A qtd de números pares é: ", par) 
print("A qtd de números ímpares é: ", impar) 