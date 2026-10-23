"""Запуск пакета shop як програми: python -m shop."""

from .cart import add_to_cart
from .payments.card import pay


def main() -> None:
    print(f"add_to_cart(1) = {add_to_cart(1)}")
    print(pay(250))


if __name__ == "__main__":
    main()
