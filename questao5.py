score = 0
a = input().upper().strip()
if a == "S" or a == "SIM":
    score = score + 1

b = input().upper().strip()
if b == "S" or b == "SIM":
    score = score + 1

c = input().upper().strip()
if c == "S" or c == "SIM":
    score = score + 1

d = input().upper().strip()
if d == "S" or d == "SIM":
    score = score + 1

e = input().upper().strip()
if e == "S" or e == "SIM":
    score = score + 1

def crime():
    if score == 2:
        print("Suspeito")
    elif score == 3 or score == 4:
        print("Cúmplice")
    elif score == 5:
        print("Assassino")
    else:
        print("Inocente")

resultado = crime()
