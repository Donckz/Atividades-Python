vel = float(input('Qual é a velocidade atual do carro? '))
mu = (vel - 80)*7.00
if vel <=80:
    print('Você está em uma otima velocidade! Boa viagem.')
else:
    print('MULTADO! deverá pagar uma multa de R${:.2f}'.format(mu))