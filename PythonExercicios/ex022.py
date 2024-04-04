nome = str(input('Digite seu nome: ')).strip() #tirar espaços inúteis

print('Nome com letras maiúsculas: {}'.format(nome.upper()))

print('Nome com letras minúsculas: {}'.format(nome.lower()))

print('Quantidade de caractéres incluindo espaços: {}'.format(len(nome)))

print('Quantidade de caractéres sem espaço: {}'.format(len((''.join(nome.split())))))

#print('Quantidade de caractéres do primeiro nome: {}'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
