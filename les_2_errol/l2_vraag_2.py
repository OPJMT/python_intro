from math import sqrt

#functie waar x wordt gebruikt in de berekening
def vraag2(x):
    return sqrt(3*x - 1) + ((1 + x) ** 2)

#waarde toewijzen aan x
x = 9.1

#functie gebruiken met x, deze functie returned een waarde die wordt opgeslagen in y
y = vraag2(x)

#output
print(f"De waarde van {y} als x = {x}")