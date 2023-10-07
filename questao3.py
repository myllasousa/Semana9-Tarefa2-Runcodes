def data_valida(data):
    if len(data) != 8:
        return False

    dia = int(data[0:2])
    mes = int(data[2:4])
    ano = int(data[4:8])

    if mes < 1 or mes > 12:
        return False

    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia < 1 or dia > 31:
            return False
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia < 1 or dia > 29:
                return False
        else:
            if dia < 1 or dia > 28:
                return False
    else:
        if dia < 1 or dia > 30:
            return False

    return True

data = input("")

if data_valida(data):
    print(True)
else:
    print(False)
