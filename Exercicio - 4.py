n = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(n))
print('É um número?', n.isnumeric())
print('É alfanúmerico?', n.isalnum())
print('É alfabético?', n.isalpha())
print('Só tem espaços?', n.isspace())
print('Está em maiusculas?', n.isupper())
print('Está em minusculas?', n.islower())
print('Está capitalizada?', n.istitle())