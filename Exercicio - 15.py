dias = float(input('Quantos dias o carro ficou alugado? '))
km = int(input('Quantos Km rodados? '))
print('Você deverar pagar R${:.2f}'.format(dias*60+km*0.15))