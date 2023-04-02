from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-'*20)
com = randint(0, 5) #sorteia um numero
n1 = int(input('Em que numero eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if n1 == com:
    print('Parabéns você acertou!')
else:
    print('Você errou! Pensei no numero {} e não no {}!'.format(com, n1))