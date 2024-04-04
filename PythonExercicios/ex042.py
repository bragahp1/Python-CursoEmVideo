#print('-='*15)
#print('Analisador de Triângulos')
#print('-='*15)
#r1 = float(input('Primeiro segmento: '))
#r2 = float(input('Segundo segmento: '))
#r3 = float(input('Terceiro segmento: '))
#if r1 == r2 == r3 and r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('Os segmentos podem formar um triangulo equilátero.')
#
#elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1 and r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('Os segmentos podem formar um triângulo isósceles.')
#
#elif r1 != r2 != r3 and r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('Os segmentos podem formar um triângulo escaleno.')
#
#else:
#    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

print('-='*15)
print('Analisador de Triângulos')
print('-='*15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triangulo ',end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    if r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('ISÓSCELES!')
    if r1 != r2 != r3:
        print('ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')