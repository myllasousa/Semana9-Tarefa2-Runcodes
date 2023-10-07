def numero_extenso(numero):
    unidades = ["", "uma unidade", "duas unidades", "três unidades", "quatro unidades", "cinco unidades",
                "seis unidades", "sete unidades", "oito unidades", "nove unidades"]
    dezenas = ["", "uma dezena", "duas dezenas", "três dezenas", "quatro dezenas", "cinco dezenas", "seis dezenas",
               "sete dezenas", "oito dezenas", "nove dezenas"]
    centenas = ["", "uma centena", "duas centenas", "três centenas", "quatro centenas", "cinco centenas", "seis centenas",
                "sete centenas", "oito centenas", "nove centenas"]
    if numero == 0:
        return "zero"

    if numero >= 100:
        centena = numero // 100
        resto = numero % 100
        if resto == 0:
            return centenas[centena] + "."
        elif 1 <= resto <= 10:
            return centenas[centena] + " e " + numero_extenso(resto)
        elif resto == 20 or resto == 30 or resto == 40 or resto == 50 or resto == 60 or resto == 70 or resto == 80 or resto == 90:
            return centenas[centena] + " e " + numero_extenso(resto)
        else:
            return centenas[centena] + ", " + numero_extenso(resto)
    elif numero >= 10:
        dezena = numero // 10
        resto = numero % 10
        if resto == 0:
            return dezenas[dezena] + "."
        else:
            return dezenas[dezena] + " e " + numero_extenso(resto)
    else:
        return unidades[numero] + "."

numero = int(input(""))
if numero < 1000:
    extenso = numero_extenso(numero)
    print(extenso)
