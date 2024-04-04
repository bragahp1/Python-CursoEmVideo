d = float(input('Por quantos dias o carro foi alugado? '))
k = float(input('Quantos quilometros o carro rodou? '))
vt = (d*60) + (k*0.15)
print('O valor total a pagar será de R$ {:.2f}!'.format(vt))
