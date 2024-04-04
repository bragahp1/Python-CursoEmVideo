sal = float(input('Digite o seu sálario: '))
if sal > 1250:
    print('Seu salário receberá um aumento de 10%. Seu novo salário será de R$ {:.2f}.'.format(((sal/100)*10)+sal))
else:
    print('Seu salário receberá um aumento de 15%. Seu novo salário será de R$ {:.2f}.'.format(((sal/100)*15)+sal))
