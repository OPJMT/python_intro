location_options = ("hier opeten", "meenemen")
order_types = ("burgers", "drankjes")
burger_menu = ("hamburger", "cheeseburger", "big mac", "quarter pounder")
big_burgers_options = {"big mac", "quarter pounder"}
drink_types = ("warm", "koud")
warm_drink_menu = ("koffie", "cappucino", "chocolademelk")
cold_drink_menu = ("coca cola", "cola zero", "7-up", "fanta", "fristi")
burger_menu_capitalized = tuple(i.capitalize() for i in burger_menu)
warm_drink_menu_capitalized = tuple(i.capitalize() for i in warm_drink_menu)
cold_drink_menu_capitalized = tuple(i.capitalize() for i in cold_drink_menu)
x = True
print("Welkom bij McDonald's")

while x:
    location = input("Hier opeten of meenemen? [Hier opeten/Meenemen]: ")

    if location.lower() not in location_options:
        print("Unknown input, try again.")
        continue

    print(location.capitalize())
    y = True
    while y:
        order_type = input("Burgers of drankjes? [Burgers/Drankjes]: ")
        if order_type == order_types[0]:
            z = True
            while z:
                burger = input("Burgers [{}, {}, {}, {}]: ".format(*burger_menu_capitalized))
                if burger.lower() not in burger_menu:
                    print("Unknown input, try again.")
                    continue

                if burger.lower() in big_burgers_options:
                    a = True
                    while a:
                        big_burgers_option = input(f"Wilt u een {burger.capitalize()} met of zonder kaas? [Met/Zonder]: ")
                        if big_burgers_option.lower() == "met":
                            print(f"{burger.capitalize()} met kaas")
                            a = False
                            z = False
                            y = False
                        elif big_burgers_option.lower() == "zonder":
                            print(f"{burger.capitalize()} zonder kaas")
                            a = False
                            z = False
                            y = False
                        else:
                            print("Unknown input, try again.")
                            continue
                else:
                    print(burger.capitalize())
                    z = False
                    y = False


        elif order_type == order_types[1]:
            z = True
            while z:
                drink_type = input("Drankjes [Warm/Koud]: ")
                if drink_type.lower() not in drink_types:
                    print("Unknown input, try again.")
                    continue

                if drink_type.lower() == drink_types[0]:
                    a = True
                    while a:
                        warm_drink = input("Warme drank: [{}, {}, {}]: ".format(*warm_drink_menu_capitalized))
                        if warm_drink.lower() not in warm_drink_menu:
                            print("Unknown input, try again.")
                            continue
                        else:
                            print(warm_drink.capitalize())
                            a = False
                            z = False
                            y = False

                if drink_type.lower() == drink_types[1]:
                    a = True
                    while a:
                        cold_drink = input("Koude drank: [{}, {}, {}, {}, {}]: ".format(*cold_drink_menu_capitalized))
                        if cold_drink.lower() not in cold_drink_menu:
                            print("Unknown input, try again.")
                            continue
                        else:
                            print(cold_drink.capitalize())
                            a = False
                            z = False
                            y = False
        else:
            print("Unknown input, try again.")
            continue

    if location.lower() == location_options[0]:
        print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant!")
        x = False
    else:
        print("Bedankt voor uw bestelling, goede reis en eet smakelijk!")
        x = False