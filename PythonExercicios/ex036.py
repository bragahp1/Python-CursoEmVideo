#casa = float(input('Qual é o valor da casa? '))
#salário = float(input('Qual é o valor do seu salário atual? '))
#ano = int(input('Em quantos anos você pretende pagar? '))
#prestação = casa / (ano * 12)
#minimo = (salário/100) * 30
#print('Você pretende pagar em {:0} meses, com parcelas no valor de R$ {:.2f}'.format((ano * 12), prestação))
#if prestação <= minimo:
#    print('Seu empréstimo foi aprovado!')
#else:
#    print('Seu empréstimo não foi aprovado! Para que ele seja aprovado o valor das parcelas deve ser inferior R$ {:.2f}, que seria 30% do seu salário. '.format((salário/100) * 30))

casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = (salário / 100) * 30
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
