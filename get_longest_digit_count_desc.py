def is_digit_count_desc(lst: list[int]) -> bool:
    """
    Verifica daca numarul de cifre ale elementelor listei sunt in ordine descrescatoare.
    :param lst: Lista verificata.
    :return: True daca sunt in ordine descrescatoare, False daca nu.
    """
    for i in range(1, len(lst)):
        if len(str(lst[i])) >= len(str(lst[i-1])):
            return False

    return True


def test_is_digit_count_desc():
    """"
    Verifica functia is_digit_count_desc
    """
    assert is_digit_count_desc([]) == True
    assert is_digit_count_desc([534, 422, 29, 53, 2]) == False
    assert is_digit_count_desc([522, 22, 2]) == True
    assert is_digit_count_desc([222, 22, 222]) == False
    assert is_digit_count_desc([24]) == True


def get_longest_digit_count_desc(lst: list[int]) -> list[int]:
    """
    Returneaza cea mai lunga subsecventa de numere cu numarul cifrelor in ordine descrescatoare.
    :param lst: Lista verificata.
    :return: Cea mai lunga subsecventa care indeplindeste cerinta.
    """
    subsecventa = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if is_digit_count_desc(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventa):
                subsecventa = lst[i:j + 1]
    return subsecventa


def test_get_longest_digit_count_desc():
    """
    Verifica functia get_longest_digit_count_desc
    """
    assert get_longest_digit_count_desc([]) == []
    assert get_longest_digit_count_desc([534, 43, 6543, 542, 24, 456]) == [6543, 542, 24]
    assert get_longest_digit_count_desc([53]) == [53]
    assert get_longest_digit_count_desc([532, 42, 3, 5467, 352, 53, 3]) == [5467, 352, 53, 3]


test_is_digit_count_desc()
test_get_longest_digit_count_desc()
