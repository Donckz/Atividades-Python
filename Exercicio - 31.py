dis = float(input('Olá, bom dia! \nQual distancia da sua viagem?: '))
if dis <= 200:
    don = dis*0.50
    print('Sua passagem é de R${}'.format(don))
else:
    din = dis*0.45
    print('Sua passagem por abaixo de 200Km ficou R${:.2f}'.format(din))