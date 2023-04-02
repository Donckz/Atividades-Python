titulo = '10 TERMOS DE UMA PA'
print('='*30)
print(titulo.center(30, ' '))
print('='*30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
décimo = termo + (10 - 1) * razao
for c in range(termo, décimo + razao, razao):
    print('{}'.format(c), end=' → ')
print('Acabou')