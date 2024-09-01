def add(input1, input2):
    print(input1 + input2)


def subtract(input1, input2):
    print(input1 - input2)


def multiply(input1, input2):
    print(input1 * input2)


def divide(input1, input2):
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

    if operator == operators[0]:
        add(input1, input2)
        break
    elif operator == operators[1]:
        subtract(input1, input2)
        break
    elif operator == operators[2]:
        multiply(input1, input2)
        break
    else:
        divide(input1, input2)
        break





