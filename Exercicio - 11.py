larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura? '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m²'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))