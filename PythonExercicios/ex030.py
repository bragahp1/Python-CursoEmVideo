#n = int(input('Digite um número para saber se ele é par ou impar: '))
#if n % 2 == 1:
#    print('Ele é impar!')
#else:
#    print('Ele é par!')

número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é IMPAR'.format(número))
