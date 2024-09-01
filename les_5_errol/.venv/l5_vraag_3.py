# We hebben de random module nodig om willekeurige getallen te genereren
import random
# Totaal aantal getallen op de kaart zal hoogte x breedte zijn
bingo_number_total = 4 ** 2
# Daarna maken we een lijst met 99 getallen waar we uit gaan kiezen
numbers_all = list(range(1, 100))
# We gooien alle ballen door elkaar
random.shuffle(numbers_all)
# ..en pakken de eerste 16 getallen
bingo_numbers = numbers_all[:bingo_number_total]
bingo_numbers_check = bingo_numbers.copy()

# opdracht 1
bingo_card = []
for i in range(4):
    row = []
    for i in range(4):
        row.append(bingo_numbers.pop())
    bingo_card.append(row)

for row in bingo_card:
    print(row)
print()

# opdracht 2
random.shuffle(numbers_all)
ran_50 = numbers_all[:50]
for num in ran_50:
    if num in bingo_numbers_check:
        for i in range(4):
            for j in range(4):
                if num == bingo_card[i][j]:
                    bingo_card[i][j] = 0

for row in bingo_card:
    print(row)
print()

# opdracht 3
locations = []
for i in range(4):
    for j in range(4):
        if bingo_card[i][j] == 0:
            locations.append((i, j))


def check_horizontals(locations):
    prev = locations[0]
    x = 1
    for i in locations[1:]:
        if i[0] == prev[0]:
            x += 1
            prev = i
            if x == 4:
                return "Horizontal Bingo!"
        else:
            prev = i
            x = 1


def check_verticals(bingo_card):
    for i in range(4):
        temp = []
        for j in range(4):
            if bingo_card[j][i] == 0:
                temp.append(bingo_card[j][i])
            else:
                continue
            if len(temp) == 4:
                return "Vertical Bingo!"


def check_diagonals(bingo_card):
    for i in range(4):
        if bingo_card[i][i] == 0:
            if i == 3:
                return "Diagnal Bingo!"
            continue
        else:
            break

    x = 0
    y = 3
    for i in range(4):
        if bingo_card[y][x] == 0:
            if x == 3:
                return "Diagonal Bingo!"
            x+=1
            y-=1
            continue
        else:
            break


print(check_horizontals(locations))
print(check_verticals(bingo_card))
print(check_diagonals(bingo_card))