text = """
У світі програмування існує багато алгоритмів для пошуку підрядків у тексті. Найвідомішими з них є алгоритми Кнута-Морріса-Пратта, Рабіна-Карпа та Боєра-Мура. Кожен з цих алгоритмів має свої переваги та недоліки.
"""

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            return True  # Знайдено
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False  # Не знайдено



def rabin_karp_search(text, pattern):
    d = 256  # Кількість символів в алфавіті
    q = 101  # Просте число для модуляції
    m = len(pattern)
    n = len(text)
    p = 0  # Хеш для шаблону
    t = 0  # Хеш для тексту
    h = 1

    if m > n:
        return False

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return True  # Знайдено
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return False  # Не знайдено


def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)

    if m == 0:
        return False

    skip = {}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1

    i = m - 1
    while i < n:
        j = m - 1
        k = i
        while j >= 0 and text[k] == pattern[j]:
            j -= 1
            k -= 1
        if j == -1:
            return True  # Знайдено
        else:
            i += skip.get(text[i], m)
    return False  # Не знайдено


import timeit

# Підготовка функцій для timeit
def test_kmp_existing():
    return kmp_search(text, "алгоритми")

def test_kmp_non_existing():
    return kmp_search(text, "машинне навчання")

def test_rabin_karp_existing():
    return rabin_karp_search(text, "алгоритми")

def test_rabin_karp_non_existing():
    return rabin_karp_search(text, "машинне навчання")

def test_boyer_moore_existing():
    return boyer_moore_search(text, "алгоритми")

def test_boyer_moore_non_existing():
    return boyer_moore_search(text, "машинне навчання")


# Кількість повторень для усереднення часу
number = 10000

# Існуючий підрядок
kmp_time_existing = timeit.timeit(test_kmp_existing, number=number)
rabin_karp_time_existing = timeit.timeit(test_rabin_karp_existing, number=number)
boyer_moore_time_existing = timeit.timeit(test_boyer_moore_existing, number=number)

# Неіснуючий підрядок
kmp_time_non_existing = timeit.timeit(test_kmp_non_existing, number=number)
rabin_karp_time_non_existing = timeit.timeit(test_rabin_karp_non_existing, number=number)
boyer_moore_time_non_existing = timeit.timeit(test_boyer_moore_non_existing, number=number)

# Виведення результатів
print("Результати для існуючого підрядка 'алгоритми':")
print(f"КМП: {kmp_time_existing} секунд")
print(f"Рабін-Карп: {rabin_karp_time_existing} секунд")
print(f"Боєр-Мур: {boyer_moore_time_existing} секунд\n")

print("Результати для неіснуючого підрядка 'машинне навчання':")
print(f"КМП: {kmp_time_non_existing} секунд")
print(f"Рабін-Карп: {rabin_karp_time_non_existing} секунд")
print(f"Боєр-Мур: {boyer_moore_time_non_existing} секунд")