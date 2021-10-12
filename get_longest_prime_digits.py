def is_prime(n: int) -> bool:
    """
    Verifica un numar daca este prim sau nu.
    :param n: Numarul intreg ce urmeaza a fi verificat.
    :return: True daca e prim, False daca nu e prim.
    """
    if n < 2:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for i in range(3, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    """
    Verifica functia is_prime
    """
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(2) == True
    assert is_prime(37) == True


def only_prime_digits(n: int) -> bool:
    """
    Verifica daca un numar are toate cifrele prime.
    :param n: Numarul ce urmeaza a fi verificat.
    :return: True daca numarul are toate cifrele prime, False daca nu.
    """
    while n:
        if not is_prime(n % 10):
            return False
        n //= 10

    return True


def test_only_prime_digits():
    """
    Verifica functia only_prime_digits
    """
    assert only_prime_digits(3333) == True
    assert only_prime_digits(277) == True
    assert only_prime_digits(0) == True
    assert only_prime_digits(574) == False
    assert only_prime_digits(4) == False


def list_prime_digits(lst: list[int]) -> bool:
    """
    Verifica daca toate numerele dintr-o lista au toate cifrele prime.
    :param lst: Lista ce urmeaza a fi verificata.
    :return: True daca toate numerele listei au toate cifrele prime, False daca nu.
    """
    for x in lst:
        if not only_prime_digits(x):
            return False

    return True


def test_list_prime_digits():
    """
    Verifica functia list_prime_digits
    """
    assert list_prime_digits([33, 277]) == True
    assert list_prime_digits([11, 34]) == False
    assert list_prime_digits([]) == True
    assert list_prime_digits([33, 22, 49, 34]) == False


def get_longest_prime_digits(lst: list[int]) -> list[int]:
    """
    Returneaza cea mai lunga subsecventa de numere cu toate cifrele prime.
    :param lst: Lista ce urmeaza a fi verificata.
    :return: Cea mai lunga subsecventa de numere cu toate cifrele prime.
    """
    subsecventa = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if list_prime_digits(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventa):
                subsecventa = lst[i:j + 1]
    return subsecventa


def test_get_longest_prime_digits():
    """
    Verifica functia get_longest_prime_digits
    """
    assert get_longest_prime_digits([]) == []
    assert get_longest_prime_digits([1]) == []
    assert get_longest_prime_digits([11, 21, 33, 54]) == [33]
    assert get_longest_prime_digits([24, 121, 23, 55, 17, 73]) == [23, 55]
    assert get_longest_prime_digits([222, 3232, 7277]) == [222, 3232, 7277]


test_is_prime()
test_only_prime_digits()
test_list_prime_digits()
test_get_longest_prime_digits()
