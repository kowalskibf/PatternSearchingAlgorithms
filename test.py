from naive import naive_find
from KMP import KMP_find
from RK import RK_find
from naive2 import N


def find_all(pattern, data):
    if pattern == "" or data == "" or len(pattern) > len(data):
        return None

    results = []
    i = 0

    while i < len(data):
        index = data.find(pattern, i)

        if index == -1:
            break

        results.append(index)
        i = index + 1

    return results


if __name__ == "__main__":
    with open('pan-tadeusz.txt', 'r') as file:
        data = file.read()

#zwykle napisy
    word = "Adam Mickiewicz"
    assert find_all(word, data) == naive_find(word, data) == N(word, data) == KMP_find(word, data) == RK_find(word, data)
    print(find_all(word, data))


    word = "Telimena"
    assert find_all(word, data) == naive_find(word, data) == N(word, data) == KMP_find(word, data) == RK_find(word, data)
    print(find_all(word, data))


    word = "Zosia"
    assert find_all(word, data) == naive_find(word, data) == N(word, data) == KMP_find(word, data) == RK_find(word, data)
    print(find_all(word, data))


#napis nie wystepuje
    word = "amogus"
    assert find_all(word, data) == naive_find(word, data) == N(word, data) == KMP_find(word, data) == RK_find(word, data)
    print(find_all(word, data))


#ostatni element tekstu
    word = "978-83-288-2495-9"
    assert find_all(word, data) == naive_find(word, data) == N(word, data) == KMP_find(word, data) == RK_find(word, data)
    print(find_all(word, data))

#pusty napis
    word = ""
    assert find_all(word, data) == naive_find(word, data) == N(word, data) == KMP_find(word, data) == RK_find(word, data)
    print(find_all(word, data))

#napis rowny dlugosci tekstu
    data = data[0:4]
    word = "Adam"
    assert find_all(word, data) == naive_find(word, data) == N(word, data) == KMP_find(word, data) == RK_find(word, data)
    print(find_all(word, data))

#napis dluzszy od dlugosci tekstu
    word = "Mickiewicz"
    assert find_all(word, data) == naive_find(word, data) == N(word, data) == KMP_find(word, data) == RK_find(word, data)
    print(find_all(word, data))

#tekst pusty
    data = ""
    assert find_all(word, data) == naive_find(word, data) == N(word, data) == KMP_find(word, data) == RK_find(word, data)
    print(find_all(word, data))
