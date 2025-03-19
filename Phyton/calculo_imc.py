#Atividade 7 - Cálculo do IMC.
print('Olá! calcule o seu Índice de Massa Corporal (IMC)')

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))

imc = peso / (altura ** 2)

print(f'Seu IMC é: {imc:.2f}')
