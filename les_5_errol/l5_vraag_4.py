def prime_num(num):
        if num < 2:
            return False
        x = 2
        while num >= x:
            if num == x:
                return True
            elif num % x == 0:
                return False
            else:
                x+=1


state = True
while state:
    num = input("Geef een getal: ")
    if num == ".":
        state = False
    if num.isnumeric():
        num = int(num)
        if prime_num(num):
            print(f"{num} is een priemgetal")
        else:
            print(f"{num} is geen priemgetal")

print("Tot ziens!")

