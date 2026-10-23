"""Демонстрація базових типів даних у Python."""


def basic_types_demo() -> None:
    """Виводить приклади всіх базових типів."""
    number: int = 42
    ratio: float = 3.14
    complex_number: complex = 1 + 2j
    flag: bool = True
    text: str = "Привіт"
    data: bytes = b"python"
    mutable_data: bytearray = bytearray(b"abc")
    items: list[int] = [1, 2, 3]
    pair: tuple[int, str] = (1, "два")
    unique: set[int] = {1, 2, 3}
    immutable: frozenset[int] = frozenset({4, 5, 6})
    mapping: dict[str, int] = {"один": 1, "два": 2}
    numbers_range: range = range(1, 5)
    nothing: None = None

    print(f"int: {number}")
    print(f"float: {ratio}")
    print(f"complex: {complex_number}")
    print(f"bool: {flag}")
    print(f"str: {text}")
    print(f"bytes: {data}")
    print(f"bytearray: {mutable_data}")
    print(f"list: {items}")
    print(f"tuple: {pair}")
    print(f"set: {unique}")
    print(f"frozenset: {immutable}")
    print(f"dict: {mapping}")
    print(f"range: {numbers_range}")
    print(f"None: {nothing}")
    return None


class TypesDemo:
    """Клас-обгортка для демонстрації базових типів."""

    def basic_types(self) -> None:
        """Робить те саме, що й basic_types_demo()."""
        basic_types_demo()
        return None


if __name__ == "__main__":
    print("=== Базові типи (функція) ===")
    basic_types_demo()
    print("=== Базові типи (клас) ===")
    TypesDemo().basic_types()
