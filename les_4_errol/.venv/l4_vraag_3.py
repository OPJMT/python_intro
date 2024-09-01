movies = \
{
    "The Simpsons": "636-555-3226",
    "Vegas Vacation": "555-0100",
    "Ghostbusters": "555-23678",
    "Billy Madison": "555-0840",
    "Swingers": "213-555-4679",
    "Bruce Almighty": "555-0123",
    "Seinfeld": "555-FILK",
    "Arrested Development": "555-0113",
    "Die Hard With a Vengeance": "555-0001",
    "The A-Team": "555-6162"
}

# a
print(f"Het telefoonnummer van Bruce Almighty is {movies['Bruce Almighty']}.\n")
print(f"{movies}\n")

# b
movies["Harry Potter"] = "605-475-6961"
print(f"{movies}\n")

# c
old_num_gb = movies["Ghostbusters"]
movies["Ghostbusters"] = "555-2368"
print(f"Het telefoonnummer {old_num_gb} van de Ghostbusters is gewijzigd naar {movies["Ghostbusters"]}.")
print(f"{movies}\n")

# d
rip_seinfeld = movies.pop("Seinfeld")
print(f"Telefoonnummer {rip_seinfeld} van Seinfeld is verwijderd.")
print(f"{movies}\n")

# e
print(f"In de dictionary zitten {len(movies)} telefoonnummers.")
print(movies)
