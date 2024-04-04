#n1 = float(input('Primeira nota: '))
#n2 = float(input('Segunda nota: '))
#m = (n1 + n2)/2
#if m < 5.0:
#    print('Sua média foi de {}, está abaixo de 5.0. REPROVADO.'.format(m))
#elif m >= 5.0 and m <= 7:
#    print('Sua média foi de {}, você está de recuperação.'.format(m))
#else:
#    print('Sua média foi de {}, superior a 7.0. Você está aprovado.'.format(m))

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, e a média do aluno é {:.1f}'.format(n1, n2, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está APROVADO.')
