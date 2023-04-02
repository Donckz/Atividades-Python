from random import randint
from time import sleep
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
[3] AÇO''')
jogador = int(input('Qual é a sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('═=═'*8)
computador = randint(0, 3)
                                            #JOGO DA PEDRA
if jogador == 0 and computador == 0:
    print('''COMPUTADOR JOGOU PEDRA!
JOGADOR JOGOU PEDRA!''')
    print('═=═'*8)
    if jogador == 0 and computador == 0:
        print('JOGO EMPATOU!')
elif jogador == 0 and computador == 1:
    print('''COMPUTADOR JOGOU PAPEL!
JOGADOR JOGOU PEDRA!''')
    print('═=═'*8)
    if jogador == 0 and computador == 1:
        print('JOGADOR PERDEU!')
elif jogador == 0 and computador == 2:
    print('''COMPUTADOR JOGOU TESOURA!
JOGADOR JOGOU PEDRA!''')
    print('═=═'*8)
    if jogador == 0 and computador == 2:
        print('JOGADOR GANHOU!')
                                            #JOGO DO PAPEL
if jogador == 1 and computador == 1:
    print('''COMPUTADOR JOGOU PAPEL!
JOGADOR JOGOU PAPEL!''')
    print('═=═'*8)
    if jogador == 1 and computador == 1:
        print('JOGO EMPATOU!')
elif jogador == 1 and computador == 0:
    print('''COMPUTADOR JOGOU PEDRA!
JOGADOR JOGOU PAPEL!''')
    print('═=═'*8)
    if jogador == 1 and computador == 0:
        print('JOGADOR GANHOU!')
elif jogador == 1 and computador  == 2:
    print('''COMPUTADOR JOGOU PAPEL!
JOGADOR JOGOU TESOURA!''')
    print('═=═'*8)
    if jogador == 1 and computador == 2:
        print('JOGADOR PERDEU!')
                                             #JOGO DA TESOURA
if jogador == 2 and computador == 2:
    print('''COMPUTADOR JOGOU TESOURA!
JOGADOR JOGOU TESOURA!''')
    print('═=═'*8)
    if jogador == 2 and computador == 2:
        print('JOGO EMPATOU!')
elif jogador == 2 and computador == 0:
    print('''COMPUTADOR JOGOU PEDRA!
JOGADOR JOGOU TESOURA!''')
    print('═=═'*8)
    if jogador == 2 and computador == 0:
        print('JOGADOR PERDEU!')
elif jogador == 2 and computador == 1:
    print('''COMPUTADOR JOGOU PAPEL!
JOGADOR JOGOU TESOURA!''')
    print('═=═'*8)
    if jogador == 2 and computador == 1:
        print('JOGADOR GANHOU!')
if jogador >= 4:
    print('NUMERO INVALIDO!')
                                                 #JOGO DO AÇO
if jogador == 3 and computador == 0:
    print('''COMPUTADOR JOGOU PEDRA!
JOGADOR JOGOU AÇO!''')
    print('═=═'*8)
    if jogador == 3 and computador == 0:
        print('JOGADOR GANHOU!')
if jogador == 3 and computador == 1:
    print('''COMPUTADOR JOGOU PAPEL!
JOGADOR JOGOU AÇO!''')
    print('═=═'*8)
    if jogador == 3 and computador == 1:
        print('JOGADOR GANHOU!')
if jogador == 3 and computador == 2:
    print('''COMPUTADOR JOGOU TESOURA!
JOGADOR JOGOU AÇO!''')
    print('═=═'*8)
    if jogador == 3 and computador == 2:
        print('JOGADOR GANHOU!')
if jogador == 3 and computador == 3:
    print('''COMPUTADOR JOGOU AÇO!
JOGADOR JOGOU AÇO!''')
    print('═=═'*8)
    if jogador == 3 and computador == 3:
        print('JOGADO EMPATOU!')
if jogador >= 4:
    print('NUMERO INVALIDO!')
                                           #NUMERO INVALIDO