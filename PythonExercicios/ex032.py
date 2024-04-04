from datetime import date
ano = int(input('Digite um ano para saber se é um ano bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))


#Ano bissexto são múltiplos de 4.
# Não inclui múltiplos de 100 e 400.