print('-=-'*10)
print('Olá, seja bem vindo(a)!')
print('-=-'*10)
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o quanto você recebe: R$'))
anos = int(input('Quantos anos deseja pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos\nA prestação será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Empresto pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')