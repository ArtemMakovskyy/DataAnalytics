"""Прості математичні функції для демонстрації модулів."""

PI = 3.14159


def add(a: int, b: int) -> int:
    """Повертає суму двох чисел."""
    return a + b


def circle_area(radius: float) -> float:
    """Обчислює площу круга за радіусом."""
    return PI * radius**2


class Calculator:
    """Калькулятор з базовими операціями."""

    def multiply(self, a: float, b: float) -> float:
        """Повертає добуток двох чисел."""
        return a * b


if __name__ == "__main__":
    print(f"add(2, 3) = {add(2, 3)}")
