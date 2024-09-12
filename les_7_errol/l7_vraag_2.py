def add(input1, input2, dbg=False):
    if dbg == True:
        print(f"Debug: {input1} + {input2}")
        print(input1 + input2)
        if input1 == 0 or input2 == 0:
            print("@@wAaRScHUwinG@@ Eén van de gegeven getallen is 0!")
    else:
        print(input1 + input2)


def subtract(input1, input2, dbg=False):
    if dbg == True:
        print(f"Debug: {input1} - {input2}")
        print(input1 - input2)
        if input1 == 0 or input2 == 0:
            print("@@wAaRScHUwinG@@ Eén van de gegeven getallen is 0!")
    else:
        print(input1 - input2)


def multiply(input1, input2, dbg=False):
    if dbg == True:
        print(f"Debug: {input1} * {input2}")
        print(input1 * input2)
        if input1 == 0 or input2 == 0:
            print("@@wAaRScHUwinG@@ Eén van de gegeven getallen is 0!")
    else:
        print(input1 * input2)


def divide(input1, input2, dbg=False):
    if dbg == True:
        print(f"Debug: {input1} / {input2}")
        if input2 == 0:
            print("Cannot divide by zero!")
        else:
            print(input1 / input2)

        if input1 == 0 or input2 == 0:
            print("@@wAaRScHUwinG@@ Eén van de gegeven getallen is 0!")
    else:
        if input2 == 0:
            print("Cannot divide by zero!")
        else:
            print(input1 / input2)


operators = ("+", "-", "*", "/")

while True:
    input1 = input('Geef het eerste getal: ')
    if not input1.isnumeric():
        continue
    input1 = int(input1)

    input2 = input('Geef het tweede getal: ')
    if not input2.isnumeric():
        continue
    input2 = int(input2)

    operator = input('Geef de operator (+, -, * of /): ')
    if not operator in operators:
        continue

    debug = input("Wilt u de debug informatie zien? [Ja/Nee]: ")
    if not (dbg := debug.lower()) in {"ja", "nee"}:
        continue

    if operator == operators[0]:
        if dbg == "ja":
            add(input1, input2, True)
            break
        else:
            add(input1, input2)
            break
    elif operator == operators[1]:
        if dbg == "ja":
            subtract(input1, input2, True)
            break
        else:
            subtract(input1, input2)
            break
    elif operator == operators[2]:
        if dbg == "ja":
            multiply(input1, input2, True)
            break
        else:
            multiply(input1, input2)
            break
    else:
        if dbg == "ja":
            divide(input1, input2, True)
            break
        else:
            divide(input1, input2)
            break
