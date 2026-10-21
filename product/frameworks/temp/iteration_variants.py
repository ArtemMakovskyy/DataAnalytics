"""Усі варіанти перебору (циклів) у Python: кожен варіант у своєму методі."""

from functools import reduce
from itertools import (chain, combinations, count, cycle, dropwhile, groupby,
                       islice, permutations, product, takewhile, zip_longest)
from pathlib import Path

nums = [10, 20, 30]


# 1. for по елементах (аналог for-each)
def v01_for_each():
    for x in nums:
        print(x)

    for ch in "привіт":      # рядок
        print(ch)


# 2. for з range
def v02_for_range():
    for i in range(5):              # 0..4
        print(i)

    for i in range(2, 10, 3):       # 2, 5, 8
        print(i)

    for i in range(10, 0, -1):      # у зворотному порядку
        print(i)


# 3. По індексах через len
def v03_for_len_index():
    for i in range(len(nums)):
        print(i, nums[i])


# 4. enumerate
def v04_enumerate():
    for i, x in enumerate(nums):
        print(i, x)

    for i, x in enumerate(nums, start=1):   # нумерація з 1
        print(i, x)


# 5. zip
def v05_zip():
    names = ["Оля", "Іван"]
    ages = [25, 30]
    for n, a in zip(names, ages):
        print(n, a)

    for n, a in zip_longest(names, [1], fillvalue=None):
        print(n, a)


# 6. Перебір словника
def v06_dict():
    d = {"a": 1, "b": 2}

    for k in d:
        print(k)
    for k in d.keys():
        print(k)
    for v in d.values():
        print(v)
    for k, v in d.items():
        print(k, v)


# 7. reversed і sorted
def v07_reversed_sorted():
    for x in reversed(nums):
        print(x)

    for x in sorted(nums, reverse=True):
        print(x)

    for x in nums[::-1]:
        print(x)


# 8. while
def v08_while():
    i = 0
    while i < len(nums):
        print(nums[i])
        i += 1

    # нескінченний цикл з break
    lines = iter(["a", "b", "q"])
    while True:
        line = next(lines)
        if line == "q":
            break
        print(line)

    # імітація do-while
    n = 0
    while True:
        print("Виконується мінімум раз", n)
        n += 1
        if not n < 3:
            break


# 9. break, continue, else
def v09_break_continue_else():
    for x in nums:
        if x == 20:
            continue        # пропустити ітерацію
        if x == 30:
            break           # вийти з циклу
        print(x)
    else:
        print("Цикл завершився без break")


# 10. Вкладені цикли та product
def v10_nested_and_product():
    for i in range(3):
        for j in range(3):
            print(i, j)

    for i, j in product(range(3), repeat=2):
        print(i, j)


# 11. Comprehensions
def v11_comprehensions():
    squares = [x * x for x in nums]                 # список
    evens = [x for x in nums if x % 2 == 0]         # з фільтром
    sq_set = {x * x for x in nums}                  # множина
    sq_dict = {x: x * x for x in nums}              # словник
    gen = (x * x for x in nums)                     # генератор
    print(squares, evens, sq_set, sq_dict, list(gen))


# 12. map, filter, reduce
def v12_map_filter_reduce():
    print(list(map(lambda x: x * 2, nums)))
    print(list(filter(lambda x: x > 10, nums)))
    print(reduce(lambda a, b: a + b, nums))

    for _ in map(print, nums):      # побічні ефекти (рідко)
        pass


# 13. iter / next вручну
def v13_iter_next():
    it = iter(nums)
    print(next(it))
    print(next(it, "кінець"))

    it = iter(nums)
    while True:
        try:
            x = next(it)
        except StopIteration:
            break
        print(x)


# 14. Генератори та власні ітератори
def countdown(n):
    while n > 0:
        yield n
        n -= 1


class Counter:
    def __init__(self, n):
        self.n, self.i = n, 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i


def v14_generators_and_iterators():
    for x in countdown(3):
        print(x)

    for x in Counter(3):
        print(x)


# 15. Модуль itertools
def v15_itertools():
    for i in count(1):                      # 1, 2, 3 ...
        if i > 3:
            break
        print(i)

    for x in islice(cycle("AB"), 5):        # A B A B A
        print(x)

    for x in chain([1, 2], [3, 4]):
        print(x)

    for p in permutations([1, 2, 3]):
        print(p)

    for c in combinations([1, 2, 3], 2):
        print(c)

    for x in takewhile(lambda x: x < 3, [1, 2, 3, 1]):
        print(x)

    for x in dropwhile(lambda x: x < 3, [1, 2, 3, 1]):
        print(x)

    for key, group in groupby("AAABBC"):
        print(key, list(group))


# 16. Файли, рядки, директорії
def v16_files_and_strings():
    with open(__file__, encoding="utf-8") as f:
        for line in f:                      # лінивe читання
            print(line.rstrip())
            break

    for p in Path(".").glob("*.py"):
        print(p)


# 17. Розпакування в циклі
def v17_unpacking():
    pairs = [(1, "a"), (2, "b")]
    for num, letter in pairs:
        print(num, letter)

    for first, *rest in [(1, 2, 3), (4, 5, 6)]:
        print(first, rest)


# 18. Зміна колекції під час перебору
def v18_modify_while_iterating():
    data = [10, 20, 30]
    for x in data[:]:                       # перебір копії
        if x == 20:
            data.remove(x)
    print(data)

    data = [x for x in [10, 20, 30] if x != 20]   # новий список
    print(data)


# 19. any, all, sum, min, max
def v19_any_all_sum_min_max():
    print(any(x > 25 for x in nums))
    print(all(x > 5 for x in nums))
    print(sum(x for x in nums))
    print(min(nums), max(nums))
    print(max(nums, key=lambda x: -x))


# 20. Рекурсія та стек/черга
def walk(lst):
    for item in lst:
        if isinstance(item, list):
            walk(item)
        else:
            print(item)


def v20_recursion_and_stack():
    walk([1, [2, [3, 4]], 5])

    stack = [[1, [2, [3, 4]], 5]]           # те саме через стек
    while stack:
        current = stack.pop()
        for item in reversed(current):
            if isinstance(item, list):
                stack.append(item)
            else:
                print(item)


ALL_VARIANTS = [
    v01_for_each, v02_for_range, v03_for_len_index, v04_enumerate, v05_zip,
    v06_dict, v07_reversed_sorted, v08_while, v09_break_continue_else,
    v10_nested_and_product, v11_comprehensions, v12_map_filter_reduce,
    v13_iter_next, v14_generators_and_iterators, v15_itertools,
    v16_files_and_strings, v17_unpacking, v18_modify_while_iterating,
    v19_any_all_sum_min_max, v20_recursion_and_stack,
]


if __name__ == "__main__":
    for func in ALL_VARIANTS:
        print(f"\n=== {func.__name__} ===")
        func()
