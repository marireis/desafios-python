'''4. Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21'''


n = float(input("Quanto dinheiro você tem? \nR$"))

dolar = 4.91
pesoArg = 0.02
dolarAust = 3.18
dolarCan = 3.64
franco = 0.42
euro = 5.36
libra = 6.21

conversao1 = n / dolar
conversao2 = n / pesoArg
conversao3 = n / dolarAust
conversao4 = n / dolarCan
conversao5 = n / franco
conversao6 = n / euro
conversao7 = n / libra

print("Com R${} você pode comprar em Dolar US$ {:.2f}.".format(n, conversao1))
print("Com R${} você pode comprar em Peso Argentino US$ {:.2f}.".format(n, conversao2))
print("Com R${} você pode comprar Dolar Australiano US$ {:.2f}.".format(n, conversao3))
print("Com R${} você pode comprar em Dolar Canadense US$ {:.2f}.".format(n, conversao4))
print("Com R${} você pode comprar US$ em Franco US$ {:.2f}.".format(n, conversao5))
print("Com R${} você pode comprar US$ em Euro US$ {:.2f}.".format(n, conversao6))
print("Com R${} você pode comprar em Libra US$ {:.2f}.".format(n, conversao7))
