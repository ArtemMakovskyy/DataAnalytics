"""Демонстрація різних способів імпорту модулів і пакетів."""

import math_utils
from math_utils import add, PI
import math_utils as mu

from shop import add_to_cart
from shop.payments.card import pay
from basic_types import basic_types_demo


def main() -> None:
    print("=== import math_utils ===")
    print(f"math_utils.add(2, 3) = {math_utils.add(2, 3)}")

    print("=== from math_utils import add, PI ===")
    print(f"add(4, 5) = {add(4, 5)}")
    print(f"PI = {PI}")

    print("=== import math_utils as mu ===")
    print(f"mu.circle_area(2) = {mu.circle_area(2)}")

    print("=== from shop import add_to_cart ===")
    print(f"add_to_cart(1) = {add_to_cart(1)}")

    print("=== from shop.payments.card import pay ===")
    print(pay(250))

    print("=== from basic_types import basic_types_demo ===")
    basic_types_demo()


if __name__ == "__main__":
    main()
