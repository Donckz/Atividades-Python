from datetime import date
atual = date.today().year #saber o ano
nascimento = int(input('Qual ano você nasceu? '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos. Ainda falta {} anos para o alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
        saldo = idade - 18
        print('Você ja deveria ter se alistado a {} anos'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}'.format(ano))