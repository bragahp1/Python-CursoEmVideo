#v = float(input('Digite a velocidade do carro: '))
#if v > 80:
#    print('Você ultrapassou {} km a mais do limite de velocidade. E receberá uma multa.'.format(v - 80))
#    m = (v - 80)*7
#    print('O valor da multa será de R$ {:.2f}!'.format(m))
#else:
#    print('Você está dentro do limite de velocidade permitido.')

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:  #condição simples
    print('MULTADO! Você excedeu o limite permitido que é de 80 Km/h.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
