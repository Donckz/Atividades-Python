preço = float(input('Qual o preço do produto? R$')) 
novo = preço - (preço * 5 / 100)
print('O preço final do produto com 5% desconto, ficará {:.2f}'.format(novo))