from datetime import date
print('-=-'*15)
print('Sistema de verificação de idade da CNN.')
print('-=-'*15)
idade = int(input('Ano de nascimento: '))
data = date.today().year
idades = data - idade
if idades <=9:
        print('O atleta tem {} anos.'.format(idades))
        print('Classificação: MIRIM!')
elif idades <=14:
        print('O atleta tem {} anos.'.format(idades))
        print('Classificação: INFANTIL!')
elif idades <=19:
        print('O atleta tem {} anos.'.format(idades))
        print('Classificação: JUNIOR!')
elif idades <=20:
        print('O atleta tem {} anos.'.format(idades))
        print('Classificação: SÊNIOR!')
elif idades >=20:
        print('O atleta tem {} anos.'.format(idades))
        print('Classificação: MASTER!')