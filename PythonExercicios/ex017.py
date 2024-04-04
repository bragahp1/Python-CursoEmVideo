'''from math import pow, sqrt
o = float(input('Digite o valor do cateto oposto:'))
a = float(input('Digite o valor do cateto adjacente:'))
#co = pow(o,2)
#ca = pow(a,2)
#h = sqrt(co+ca)
#print('O valor da hipotenusa é igual a {:.2f}.'.format(h))
print('O valor da hipotenusa é igual a {:.2f}.'.format(sqrt((pow(o, 2)+pow(a, 2)))))'''

'''co = float(input('Digite o valor do cateto oposto:  '))
ca = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa é igual a {:.2f}.'.format(((co**2)+(ca**2))**0.5))'''

import math
co = float(input('Digite o valor do cateto oposto:  '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa é igual a {:.2f}.'.format(hi))
