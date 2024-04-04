from random import randint, choice
#n = [0, 1, 2, 3, 4, 5]
#p = choice(n)
#e = int(input('O computador escolheu um número de 0 a 5. Tente descobrir qual valor ele escolheu: '))
#if e == p:
#    print('Parabés! Você acertou!')
#else:
#    print('Você errou. O número era {}. Tente outra vez!'.format(p))

from time import sleep
comp = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jog = int(input('Em que némero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jog == comp:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(comp, jog))
