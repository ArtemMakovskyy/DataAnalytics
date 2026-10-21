def basic_types_demo() -> None:
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
    list_value: list = [1, 2, 3]
    tuple_value: tuple = (1, 2, 3)
    set_value: set = {1, 2, 3}
    frozenset_value: frozenset = frozenset({1, 2, 3})
    dict_value: dict = {"key": "value"}

    # Діапазон
    range_value: range = range(5)

    # Відсутність значення
    none_value: None = None

    print(integer_value, float_value, complex_value, bool_value)
    print(str_value, bytes_value, bytearray_value)
    print(list_value, tuple_value, set_value, frozenset_value, dict_value)
    print(range_value, none_value)

    return None


basic_types_demo()