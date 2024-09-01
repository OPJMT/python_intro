import time

GLOB_DICT = {}


def zeef_van_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    current_prime = 2
    while current_prime * current_prime <= limit:
        if is_prime[current_prime]:
            for multiple in range(current_prime * current_prime, limit + 1, current_prime):
                is_prime[multiple] = False
        current_prime += 1

    prime_numbers = []
    for number in range(2, limit + 1):
        if is_prime[number]:
            prime_numbers.append(number)

    return prime_numbers


def check_dict(num):
    if num in GLOB_DICT:
        return GLOB_DICT[num]
    else:
        primes = zeef_van_eratosthenes(num)
        GLOB_DICT[num] = primes
        return primes


def run():
    while True:
        num = input("Voer een getal in: ")
        if not num.isnumeric():
            continue

        num = int(num)
        tijd_nu = time.time()
        primes = check_dict(num)
        tijd_verstreken = time.time() - tijd_nu
        for prime in primes:
            print(prime)
        print(f"Tijd verstreken: {tijd_verstreken}")
        print()

run()