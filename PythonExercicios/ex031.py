#p = float(input('Qual a distância da viagem em Km? '))
#if p <= 200:
#    print('Para {} Km o valor da passagem será de R$ {:.2f}.'.format(p, (p*0.50)))
#else:
#    print('Para {} Km o valor da passagem será de R$ {:.2f}.'.format(p, (p*0.45)))

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(preço))
