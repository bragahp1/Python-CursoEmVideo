f = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vezes.'.format(f.count('A')))

print('A letra a aparece pela primeira vez na posição {}'.format(f.find('A')+1))

print('A letra a aparece pela última vez na posição {}.'.format(f.rfind('A')+1))


#falha se houver espaço desnecessário entre as palavras