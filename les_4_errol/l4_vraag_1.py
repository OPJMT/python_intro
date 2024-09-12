games =\
[
    "Player’s Unknown Battle Ground (PUBG) 50 Million 2018",
    "Fortnite Battle Royale 39 Million 2017",
    "Apex Legends 50 Million (1 Month) 2019",
    "League of Legends (LOL) 27 Million 2009",
    "Counter Strike; Global Offensive 32 Million 2014",
    "Heartstone 29 Million 20120",
    "Minecraft 91 Million 2011",
    "DOTA 2 5 million 2015",
    "The Division 2 N/A 2019",
    "Splatoon 2"
]

# a
print(f"5, {games[4]}")
print(f"{games}\n")

# b
print(f"The game {games[7]} has {len(games[7])} character")
print(f"{games}\n")

# c
print(f"Er zitten {len(games)} games in de lijst")
print(f"{games}\n")

# d
games.insert(1, "Snake")
print(f"{games}\n")

# e
game = games.pop(10)
print(f"Helaas heeft de game {game} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {game}.")
print(f"{games}\n")

# f
x = games[6].replace("20120", "2012")
games[6] = x
print(games)