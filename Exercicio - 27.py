from stat import FILE_ATTRIBUTE_OFFLINE


n = str(input('Qual seu nome completo? ')).strip()
nome = n.split()
print('Muito prazer em te conhecer {}!'.format(n))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))