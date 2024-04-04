num = int(input('Digite um número: '))
print('1 - para converter para binário'
      '\n2 - para octal'
      '\n3 - para hexadecimal')
esc = int(input('Escolha uma opção: '))
if esc == 1:
    print('{} convertido para biário é igual a {}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Escolha uma opção válida.')
