# Ordering at McDonald's

eat_in = False
locations = {"opeten", "meenemen"}
order_types = {"burgers", "drankjes"}
burger_menu = {"hamburger", "cheeseburger", "big mac", "quarter pounder"}
drink_types = {"warme", "koude"}
warm_drinks = {"koffie", "cappucino", "chocolademelk"}
cold_drinks = {"coca cola", "cola zero", "7-up", "fanta", "fristi"}


def ask_question(question, valid_answers):
    answer = input(question)
    answer = answer.lower()
    if answer in valid_answers:
        return answer


def cap_first_letters(text):
    if " " in text:
        words = text.split(" ")
        for i in range(words_len:=(len(words))):
            words[i] = words[i].capitalize()
        text = " ".join(words)
        print(text)
    elif "-" in text:
        words = text.split("-")
        for i in range(words_len := (len(words))):
            words[i] = words[i].capitalize()
        text = "-".join(words)
        print(text)
    else:
        print(text.capitalize())


def get_location():
    while True:
        location = ask_question("Hier opeten of meenemen? [Opeten/Meenemen]: ", locations)
        if location is None:
            continue
        else:
            break

    global eat_in
    if location == "opeten":
        # Eat in part
        print("Hier opeten")
        eat_in = True
    else:
        # Take away part
        print("Meenemen")
        eat_in = False


def get_order():
    while True:
        order_type = ask_question("Burgers of drankjes? [Burgers/Drankjes]: ", order_types)
        if order_type is None:
            continue
        else:
            break
    if order_type == "burgers":
        print("Burgers")
        get_burger_choice()
    else:
        print("Drankjes")
        get_drink_choice()


def get_burger_choice():
    while True:
        burger = ask_question("Burgers [Hamburger, Cheeseburger, Big Mac, Quarter Pounder]: ", burger_menu)
        if burger is None:
            continue
        else:
            break
    cap_first_letters(burger)


def get_drink_choice():
    while True:
        drink_type = ask_question("Drankjes [Warme/Koude]: ", drink_types)
        if drink_type is None:
            continue
        else:
            break
    if drink_type == "warme":
        print("Warme")
        get_warm_drink_choice()
    else:
        print("Koude")
        get_cold_drink_choice()


def get_warm_drink_choice():
    while True:
        warm_drink = ask_question("Warme drank: [Koffie, Cappucino, Chocolademelk]: ", warm_drinks)
        if warm_drink is None:
            continue
        else:
            break
    cap_first_letters(warm_drink)


def get_cold_drink_choice():
    while True:
        cold_drink = ask_question("Koude drank: [Coca Cola, Cola Zero, 7-Up, Fanta, Fristi]: ", cold_drinks)
        if cold_drink is None:
            continue
        else:
            break
    cap_first_letters(cold_drink)


def parting_line(eat_in):
    if eat_in:
        print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant.")
    else:
        print("Bedankt voor uw bestelling, goede reis en eet smakelijk.")


print("Welkom bij McDonald's")
get_location()
get_order()
parting_line(eat_in)