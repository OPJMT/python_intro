#functie waar t, v en c worden gebruikt in de berekening
def vraag4(t,v,c):
    return t * (1 / (v * (1 - ((v ** 2) / (c ** 2)))))

#waardes toewijzen aan variabelen
t = 4
v = 179875474.8
c = 299792458

#functie gebruiken met de toegewezen variabelen, deze functie returned een waarde die wordt opgeslagen in y
y = vraag4(t, v, c)

# output
print(f"Vanaf een komeet gezien zit u {y} uur op de tuinstoel.")
print(f"Vanaf een komeet gezien zit u {y * 60} minuten op de tuinstoel.")
print(f"Vanaf een komeet gezien zit u {y * 360} seconden op de tuinstoel.")