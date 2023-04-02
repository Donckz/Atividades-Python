sal = float(input('Qual seu salario atual? R$'))
if sal <=1250.00:
    ab = sal + (sal * 15 / 100)
    print('Por seu salario ser inferior a R$1250,00, receberar um aumento de 15% e ficará R${}'.format(ab))
else:
    su = sal + (sal * 10 / 100)
    print('Por seu salario ser superior a R$1250,00, receberar um aumento de 10% e ficará R${}'.format(su))