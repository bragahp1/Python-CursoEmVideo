#n1 = int(input('Digite um número: '))
#n2 = int(input('Digite outro: '))
#n3 = int(input('Digite outro: '))
#lis = [n1, n2, n3]
#lista = sorted(lis)
#print('O número menor será {}.'.format(lista[0]))
#print('O múmero maior será {}.'.format(lista[2]))

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é o maior
maior = a
if b > a and c > b:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
