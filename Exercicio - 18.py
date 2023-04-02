from math import sin, cos, tan, radians
an = float(input('Digite um ângulo que você deseja: '))
seno = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(an, seno))
cosseno = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(an, cosseno))
tangente = tan(radians(an))
print('O ângulo de {} tem o TANGENTE de {:.2f}.'.format(an, tangente))