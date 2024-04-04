# from datetime import date
#ano = int(input('Digite o ano do seu nascimento: '))
#alist = date.today().year - ano
#if alist < 18:
#    print('Com base no seu ano de nascimento, você tem {} anos. \nAinda vai se alistar ao serviço militar.'.format(alist))
#elif alist == 18:
#    print('Você já tem 18 anos, está na hora de se alistar.')
#else:
#    print('Com base no seu ano de nascimento, você tem mais de 18 anos.\nJá passou do tempo para se alistar.')

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
print('Seu sexo:')
print('(1) Homem\n(2) Mulher')
sexo = int(input('Sua opção: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if sexo == 2:
    print('Seu alistamento não é obrigatório!')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
