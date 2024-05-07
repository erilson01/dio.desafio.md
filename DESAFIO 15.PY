dias = int(input('quanto dias alugado?'))
km = float(input('quantos km rodado?'))
pago = (dias * 60 ) + (km * 0.15)
print('o total a pagar e de R${:.2f}'.format(pago))

