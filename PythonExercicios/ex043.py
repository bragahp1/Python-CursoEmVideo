from math import pow
print('-='*15)
print('Calculadora de Massa Corporal')
print('-='*15)
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso/(pow(altura, 2))
print('Seu IMC é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')


