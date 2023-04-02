print('-=-'*10)
print('Analisador de Triângulos')
print('-=-'*10)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='8')
    if r1 == r2 == r3:
        print('EQUILÁTERO!') 
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else :
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO podem formar triângulos!')