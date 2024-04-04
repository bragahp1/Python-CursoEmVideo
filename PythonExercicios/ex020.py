a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
list = [a1, a2, a3, a4]
print('A ordem dos alunos será {}'.format(sorted(list)))

'''from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lis = [a1, a2, a3, a4]
print('A ordem dos alunos será {}'.format(shuffle(lis)))'''

from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lis = [a1, a2, a3, a4]
shuffle(lis)
print('A ordem dos alunos será {}')
print(lis)
