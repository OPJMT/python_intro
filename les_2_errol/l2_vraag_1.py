# 331 containers gelost in 441 minuten
# 287 containers geladen in 295 minuten

#waardes toewijzen aan variabelen
unloaded_freight = 331
loaded_freight = 287
unload_time = 441
load_time = 295

#calc in minuten
time_per_unload_min = unload_time / unloaded_freight
time_per_load_min = load_time / loaded_freight

#calc rest seconden
time_per_unload_sec = time_per_unload_min * 60 % 60
time_per_load_sec = time_per_load_min * 60 % 60

#output
print(f"De gemiddelde lostijd bedraagt {int(time_per_unload_min)} minuut en {int(time_per_unload_sec)} seconden per container")
print(f"De gemiddelde laadtijd bedraagt {int(time_per_load_min)} minuut en {int(time_per_load_sec)} seconde per container")
