print('{:^40}'.format(' LOJAS BRAGA '))
vp = float(input('Preço das compras: R$ '))
print('''Formas de pagamentos
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = vp - ((vp/100)*10)
elif opção == 2:
    total = vp - ((vp/100)*5)
elif opção == 3:
    total = vp
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ de {:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = vp + ((vp/100)*20)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totalparc, parcela))
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
    total = 0
print('A sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(vp, total))
