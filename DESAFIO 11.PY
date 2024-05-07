larg = float(input('largura da parede:'))
alt = float(input('altura da parede'))
area = larg * alt
print('sua parede tem dimensao {:.2f}x{:.2f} e sua area e de{:.2f}m²'.format(larg, alt, area))
tinta = area / 2
print('para pinta a parede voce precisaria de {:.2f}L de tinta'.format(tinta))