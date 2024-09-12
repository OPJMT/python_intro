x = True
options = ("4g","5g","wifi open")

while x:
    connection = input("Welke verbinding wilt U gebruiken? [4G, 5G, Wifi open]: ")

    if connection.lower() not in options:
        print("Onbekende invoer, er wordt geen verbinding tot stand gebracht.")

    if connection.lower() == "4g":
        print("U bent verbonden via 4G!")
        x = False

    if connection.lower() == "5g":
        print("U bent verbonden via 5G!")
        x = False

    if connection.lower() == "wifi open":
        print("U heeft voor Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.")
        answer = input("Wilt u nog steeds een verbinding maken? [ja/nee]: ")
        if answer.lower() == "ja":
            print("U bent verbonden via Wifi open!")
            x = False
        elif answer.lower() == "nee":
            print("U bent niet verbonden.")
        else:
            print("Onbekende invoer, er wordt geen verbinding tot stand gebracht.")