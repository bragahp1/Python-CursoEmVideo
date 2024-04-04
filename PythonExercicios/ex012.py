n = float(input('Qual o preço do produto? '))
d = n-(n/100*5)
print('O valor do produto que custava R$ {:.2f}, com 5% de desconto será {:.2f}.'.format(n, d))