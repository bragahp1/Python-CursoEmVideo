from random import choice
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
l = [a, b, c, d]
alu = choice(l)
print('O aluno sorteado foi {}.'.format(alu))
