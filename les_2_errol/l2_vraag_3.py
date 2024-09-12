from math import sqrt

#functie waar a, b en c worden gebruikt in de berekening
def vraag3(a,b,c):
    return (-abs(b) + sqrt(b ** 2 - 4 * a * c)) / (2 * a)

#waardes toewijzen aan variabelen
a = 0.87
b = 22.7
c = 5.03

#functie gebruiken met de toegewezen variabelen, deze functie returned een waarde die wordt opgeslagen in y
y = vraag3(a,b,c)

# output
print(f"De waarde van y = {y} als a = {a}, b = {b} en c = {c}")

