n = (input('Digite algo:'))
print('O tipo primitivo desse valor é', type(n))
print('É alfanumérico?', n.isalnum())
print('É alfabético?', n.isalpha())
print('É decimal?', n.isdecimal())
print('Só tem espaço?', n.isspace())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('Está captalizada?', n.istitle())