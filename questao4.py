morango = float(input(""))
maca = float(input(""))

def valor_morango():
    if morango <= 5:
        return morango * 2.50
    elif morango > 5:
        return morango * 2.20

def valor_maca():
    if maca <= 5:
        return maca * 1.80
    elif maca > 5:
        return maca * 1.50

valor_mo = valor_morango()
valor_ma = valor_maca()
valor_total = valor_mo + valor_ma

def preço_pagar():
    if morango + maca > 8 or valor_total > 25.0:
        return valor_total - (valor_total * 10 / 100)
    else:
        return valor_total

resultado = preço_pagar()
print(f'{resultado:.2f}')
