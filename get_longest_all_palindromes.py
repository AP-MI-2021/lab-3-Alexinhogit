def is_palindrome(n: int) -> bool:
    """Verifica daca un numar este palindrom.
    :param n: Numarul ce va fi verificat.
    :return: Daca este sau nu palindrom
    """

    return str(n) == str(n)[::-1]


def test_is_palindrome():
    """
    Verifica functia is_palindrome
    """

    assert is_palindrome(12345) == False
    assert is_palindrome(10101) == True
    assert is_palindrome(1) == True
    assert is_palindrome(421525) == False
    assert is_palindrome(555555) == True


def palindrome_list(lst):
    """
    Verifica daca numerele dintr-o lista sunt palindroame
    :param lst: Lista ce va fi verificata
    :return: Numerele din lista care sunt palindroame
    """
    for x in lst:
        if is_palindrome(x) is False:
            return False
    return True


def test_palindrome_list():
    """
    Verifica functia palindrome_list
    """
    assert palindrome_list([]) == True
    assert palindrome_list([4, 0, 3, 6]) == True
    assert palindrome_list([55, 108, 929]) == False
    assert palindrome_list([51, 132, 419]) == False
    assert palindrome_list([12321, 222, 34343]) == True


def get_longest_all_palindromes(lst: list[int]) -> list[int]:
    """
    Returneaza cea mai lunga subsecventa de numere palindroame din lista
    :param lst: Lista cu elemente
    :return: Subsecventa cea mai lunga de palindroame
    """
    subsecventa = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if palindrome_list(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventa):
                subsecventa = lst[i:j + 1]
    return subsecventa


def test_get_longest_all_palindromes():
    """
    Verifica functia get_longest_all_palindromes
    """
    assert get_longest_all_palindromes([12, 13, 22, 333, 121, 52, 11, 4]) == [22, 333, 121]
    assert get_longest_all_palindromes([52]) == []
    assert get_longest_all_palindromes([5]) == [5]
    assert get_longest_all_palindromes([1, 2, 33, 44, 55]) == [1, 2, 33, 44, 55]


test_is_palindrome()
test_palindrome_list()
test_get_longest_all_palindromes()
