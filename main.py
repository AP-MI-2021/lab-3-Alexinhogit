from get_longest_all_palindromes import get_longest_all_palindromes
from get_longest_prime_digits import get_longest_prime_digits


def list_input() -> [int]:
    """
    Functia care permite introducerea numerelor.
    :return: Numerele introduse sub forma de lista
    """
    lst = [int(x) for x in input("Introduceti numerele listei separate cu un spatiu: ").split(" ")]

    return lst


def show_menu():
    """
    Arata meniul
    """
    print("""       Folositi "1" pentru a introduce lista, apoi alegeti una din optiunile de mai jos: 
    1. Citire date.
    2. Determinare cea mai lungă subsecvență cu toate numerele palindrom.
    3. Determinare cea mai lungă subsecvență cu toate numerele formate din cifre prime.
    4. Ieșire.""")


def main():
    lst = []
    while True:
        show_menu()
        cmd = input("Comanda: ")
        if cmd == "1":
            lst = list_input()
        elif cmd == "2":
            print(get_longest_all_palindromes(lst))
        elif cmd == "3":
            print(get_longest_prime_digits(lst))
        elif cmd == "4":
            break
        else:
            print("Comanda invalida")


if __name__ == "__main__":
    main()
