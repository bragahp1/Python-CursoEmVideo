#print('Vamos verificar se três retas podem formar um triângulo.')
#r1 = float(input('Primeira reta: '))
#r2 = float(input('Segunda reta: '))
#r3 = float(input('Terceira reta: '))
#l = [r1, r2, r3]
#t = sorted(l)
#a = (t[2]-t[1])# < t[0] < t[1] + t[2]
#b = (t[2]-t[0])# < t[1] < t[0] + t[2]
#c = (t[1]-t[0])# < t[2] < t[0] + t[1]
#if a < t[0] < t[1] + t[2] and b < t[1] < t[0] + t[2] and c < t[2] < t[0] + t[1]:
#    print('As três retas apresentadas podem formar um triângulo!')
#else:
#    print('As três retas apresentadas não podem formar um triângulo!')

print('-='*15)
print('Analisador de Triângulos')
print('-='*15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulos!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
