#Atividade 10 - Conversor de Moedas.
print('Conversão de Dolar para Real.')

taxaCambio = float(input('Insira a Taxa de Cambio: \n'))
real = float(input('Insira R$: \n'))
conver = real/taxaCambio

print(f'US${conver:.2f}')