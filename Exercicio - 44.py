print('{:=^40}'.format('LOJAS VITINHO'))
preço = float(input('Qual o preço do produto? R$'))
print('-'*45)
print('FORMAS DE PAGAMENTOS!\n[1] - Para compras AVISTA!')
print('[2] - Para compras AVISTA NO CARTÃO!')
print('[3] - Para compras em até 2X no CARTÃO!')
print('[4] - Para compras de 3X ou mais no CARTÃO!')
print('-'*45)
opção = float(input('Qual é a opção? '))

if opção == 1:
    vista = preço - (preço * 10 / 100)
    print('Recebeste um desconto de 10%, preço final do seu produto ficou: R${}'.format(vista))
elif opção == 2:
    cartao = preço - (preço * 5 / 100)
    print('Recebeste um desconto de 5%, preço final do seu produto ficou: R${}'.format(cartao))
elif opção == 3:
    parcela = preço / 2
    print('Sua compra será parcelada em 2X de R${:.2f}'.format(parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preço))
elif opção == 4:
    trinta = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas?'))
    parcela = trinta / totalparc
    print('Sua compra será parcelada em {}X de R${:.2f}'.format(totalparc, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, trinta))
else:
    print('Tente novamente, numero invalido!')