salario = float(input('Qual é o seu salario? '))
novo = salario + (salario * 15 / 100)
print('Seu salario de R${:.2f} com 15% de aumento ficou R${:.2f}!'.format(salario, novo))