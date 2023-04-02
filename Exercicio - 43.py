print('-=-'*10)
print('Calcule seu IMC!')
print('-=-'*10)
peso = float(input('Qual é seu peso? (KG): '))
altura = float(input('Qual sua altura? (m): '))
calculo = peso / (altura ** 2)
if calculo <= 18.5:
    print('O IMC dessa pessoa é de {:.1f}'.format(calculo))
    print('Você está na faixa de BAIXO PESO!')
elif calculo >=18.5 and calculo < 25:
    print('O IMC dessa pessoa é de {:.1f}'.format(calculo))
    print('Você está na faixa de PESO IDEAL!')
elif calculo >=25 and calculo < 30:
    print('O IMC dessa pessoa é de {:.1f}'.format(calculo))
    print('Você está na faixa de SOBREPESO!')
elif calculo >=30 and calculo < 40:
    print('O IMC dessa pessoa é de {:.1f}'.format(calculo))
    print('você está na faixa de OBESIDADE!')
else:
    print('O IMC dessa pessoa é de {:.1f}'.format(calculo))
    print('Você está na faixa de OBESIDADE MÓRBIDA! C-U-I-D-A-D-O!!!!')