n1 = float(input('Qual é a altura da parede? '))
n2 = float(input('Qual é a largura da parede? '))
m2 = n1*n2
print('A parede tem dimensão de {:.2f} x {:.2f} e sua área é de {:.2f} m².'.format(n1, n2, m2))
tn = m2/2
print('Para pintar essa parede, precisará de {}l de tinta.'.format(tn))
