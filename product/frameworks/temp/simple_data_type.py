def basic_types_demo() -> None:
    """
    показує базові типи даних
    Example:
    >>> integer_value = 42
    """
    # Числові типи
    integer_value: int = 42
    float_value: float = 3.14
    complex_value: complex = 2 + 3j

    # Логічний тип
    bool_value: bool = True

    # Рядок
    str_value: str = "Привіт, світе!"

    # Байти
    bytes_value: bytes = b"hello"
    bytearray_value: bytearray = bytearray(b"hello")

    # Колекції
    # list — змінюваний список, зберігає порядок, допускає дублікати.
    list_value: list = [1, 2, 3]
    list_function()
    # tuple — незмінний кортеж, зберігає порядок, допускає дублікати.
    tuple_value: tuple = (1, 2, 3)
    tuple_function()
    # set — змінювана множина унікальних елементів, без гарантованого порядку.
    set_value: set = {1, 2, 3}
    set_function()
    # frozenset — незмінна множина унікальних елементів.
    frozenset_value: frozenset = frozenset({1, 2, 3})
    frozenset_function()
    # dict — словник пар «ключ: значення», ключі унікальні, порядок вставки зберігається.
    dict_value: dict = {"key": "value"}
    dict_function()

    # Діапазон
    range_value: range = range(5)

    # Відсутність значення
    none_value: None = None

    print(integer_value, float_value, complex_value, bool_value)
    print(str_value, bytes_value, bytearray_value)
    print(list_value, tuple_value, set_value, frozenset_value, dict_value)
    print(range_value, none_value)

    return None

# list — список
def list_function() -> None:
    list_value: list = [1, 2, 3]

    list_index: int = list_value[0]  # Отримати елемент за індексом → 1
    list_find: int = list_value.index(2)  # Знайти індекс елемента → 1
    list_value.append(4)  # Додати елемент у кінець
    list_value.extend([5, 6])  # Додати кілька елементів у кінець
    list_copy: list = list_value.copy()  # Створити копію списку
    list_slice: list = list_value[1:3]  # Зріз списку
    list_sorted: list = sorted(list_value, reverse=True)  # Новий відсортований список (оригінал не змінюється)
    list_value.sort(key=lambda x: -x)  # Сортування за ключем (тут за спаданням)
    list_min: int = min(list_value)  # Найменший елемент
    list_max: int = max(list_value)  # Найбільший елемент
    list_sum: int = sum(list_value)  # Сума елементів
    list_value.insert(0, 0)  # Вставити елемент за індексом
    list_value.remove(2)  # Видалити перший елемент зі значенням 2
    list_pop: int = list_value.pop(0)  # Видалити й повернути елемент за індексом
    list_value.sort()  # Відсортувати список
    list_value.reverse()  # Розвернути порядок елементів
    list_count: int = list_value.count(1)  # Порахувати входження елемента
    list_length: int = len(list_value)  # Кількість елементів
    list_contains: bool = 2 in list_value  # Перевірити наявність елемента
    list_value.clear()  # Очистити список

    return None


# tuple — кортеж
def tuple_function() -> None:
    tuple_value: tuple = (1, 2, 3)

    tuple_index: int = tuple_value[0]  # Отримати елемент за індексом → 1
    tuple_find: int = tuple_value.index(2)  # Знайти індекс елемента → 1
    tuple_count: int = tuple_value.count(2)  # Порахувати входження елемента
    tuple_length: int = len(tuple_value)  # Кількість елементів
    tuple_slice: tuple = tuple_value[1:]  # Зріз кортежу → (2, 3)
    tuple_concat: tuple = tuple_value + (4, 5)  # Об'єднання кортежів (створює новий)
    tuple_repeat: tuple = tuple_value * 2  # Повторення кортежу
    a, b, c = tuple_value  # Розпакування кортежу
    tuple_to_list: list = list(tuple_value)  # Перетворення на список (якщо потрібно змінювати)
    tuple_sorted: list = sorted(tuple_value, reverse=True)  # Сортування повертає список
    tuple_contains: bool = 2 in tuple_value  # Перевірити наявність елемента

    return None


# set — множина унікальних елементів
def set_function() -> None:
    set_value: set = {1, 2, 3}

    set_value.add(4)  # Додати елемент
    set_value.update([5, 6])  # Додати кілька елементів
    set_value.remove(2)  # Видалити елемент (помилка, якщо його немає)
    set_value.discard(3)  # Видалити елемент без помилки, якщо його немає
    set_pop: int = set_value.pop()  # Видалити й повернути довільний елемент
    set_union: set = set_value.union({7, 8})  # Об'єднання множин
    set_intersection: set = set_value.intersection({1, 4, 5})  # Спільні елементи
    set_difference: set = set_value.difference({1})  # Різниця множин
    set_issubset: bool = set_value.issubset({1, 4, 5, 6})  # Перевірити підмножину
    set_issuperset: bool = set_value.issuperset({4})  # Перевірити надмножину
    set_symmetric: set = set_value.symmetric_difference({4, 100})  # Елементи, що є лише в одній з множин
    set_isdisjoint: bool = set_value.isdisjoint({100, 200})  # Перевірити, що немає спільних елементів
    set_copy: set = set_value.copy()  # Створити копію множини
    set_value.intersection_update({1, 4, 5, 6})  # Залишити лише спільні елементи (змінює множину)
    set_value.difference_update({1})  # Видалити елементи, що є в іншій множині (змінює множину)
    set_union_op: set = set_value | {9}  # Об'єднання через оператор
    set_inter_op: set = set_value & {4, 5}  # Перетин через оператор
    set_diff_op: set = set_value - {4}  # Різниця через оператор
    set_length: int = len(set_value)  # Кількість елементів
    set_contains: bool = 4 in set_value  # Перевірити наявність елемента
    set_value.clear()  # Очистити множину

    return None


# frozenset — незмінна множина
def frozenset_function() -> None:
    frozenset_value: frozenset = frozenset({1, 2, 3})

    frozenset_union: frozenset = frozenset_value.union({3, 4})  # Об'єднання множин
    frozenset_intersection: frozenset = frozenset_value.intersection({2, 3, 4})  # Спільні елементи
    frozenset_difference: frozenset = frozenset_value.difference({2})  # Різниця множин
    frozenset_issubset: bool = frozenset_value.issubset({1, 2, 3, 4})  # Перевірити підмножину
    frozenset_issuperset: bool = frozenset_value.issuperset({1, 2})  # Перевірити надмножину
    frozenset_symmetric: frozenset = frozenset_value.symmetric_difference({3, 4})  # Елементи лише в одній з множин
    frozenset_isdisjoint: bool = frozenset_value.isdisjoint({7, 8})  # Перевірити, що немає спільних елементів
    frozenset_copy: frozenset = frozenset_value.copy()  # Копія (повертає ту саму множину)
    frozenset_union_op: frozenset = frozenset_value | {9}  # Об'єднання через оператор
    frozenset_length: int = len(frozenset_value)  # Кількість елементів
    frozenset_contains: bool = 2 in frozenset_value  # Перевірити наявність елемента

    return None


# dict — словник пар «ключ: значення»
def dict_function() -> None:
    dict_value: dict = {"key": "value", "age": 25}

    dict_index: str = dict_value["key"]  # Отримати значення за ключем
    dict_get: str = dict_value.get("key", "")  # Отримати значення або значення за замовчуванням
    dict_setdefault: str = dict_value.setdefault("city", "Kyiv")  # Отримати або додати ключ
    dict_get_none = dict_value.get("missing")  # Поверне None, якщо ключа немає (без помилки)
    dict_value["country"] = "Ukraine"  # Додати або змінити пару
    dict_value.update({"age": 30})  # Оновити словник
    dict_value.update({"status": "Completed", "result": "Success"})  # Оновити кілька ключів і додати нові
    dict_value.update(job="Dev")  # Оновити через іменовані аргументи
    dict_copy: dict = dict_value.copy()  # Створити копію словника
    dict_fromkeys: dict = dict.fromkeys(["a", "b"], 0)  # Створити словник із ключів → {"a": 0, "b": 0}
    dict_merge: dict = dict_value | {"x": 1}  # Об'єднання словників через оператор (Python 3.9+)
    dict_sorted: dict = dict(sorted(dict_value.items()))  # Відсортований за ключами словник
    if "status" in dict_value:
        del dict_value["status"]  # Безпечно видалити ключ, лише якщо він існує
    dict_pop_safe = dict_value.pop("missing", None)  # Видалити ключ без помилки, якщо його немає
    dict_pop: int = dict_value.pop("age")  # Видалити ключ і повернути значення
    dict_popitem: tuple = dict_value.popitem()  # Видалити й повернути останню пару
    dict_keys: list = list(dict_value.keys())  # Отримати ключі
    dict_values: list = list(dict_value.values())  # Отримати значення
    dict_items: list = list(dict_value.items())  # Отримати пари ключ-значення
    dict_length: int = len(dict_value)  # Кількість пар
    dict_contains: bool = "key" in dict_value  # Перевірити наявність ключа
    dict_value.clear()  # Очистити словник

    return None

