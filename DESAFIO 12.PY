preço = float(input('qual o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('o produto que custava R${}, na promoçao de 5% vai custar R%{}'.format(preço, novo))
