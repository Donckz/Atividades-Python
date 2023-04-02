num = int(input('DIGITE UM NUMERO! '))
num2 = int(input('DIGITE OUTRO NUMERO! '))
print('='*40)
print('AGORA ESCOLHA OQUE QUER FAZER COM ELES!\n[1] - SOMAR')
print('[2] - SUBTRAIR')
print('[3] - DIVIDIR')
print('[4] - MULTIPLICAR')
opção = int(input('Sua opção: '))
if opção == 1:
    soma1 = num + num2
    print("A soma de {} com {} é {:.0f}!".format(num, num2, soma1))
elif opção == 2:
    soma2 = num - num2
    print("A subtração de {} com {} é {:.0f}!".format(num, num2, soma2))
elif opção == 3:
    soma3 = num / num2
    print('A divisão de {} com {} é {:.0f}'.format(num, num2, soma3))
elif opção == 4:
    soma4 = num * num2
    print(' A multiplicação de {} com {} é {}'.format(num, num2, soma4))
else:
    print('NÃO TEM ESSA OPÇÃO, TENTE NOVAMENTE!')