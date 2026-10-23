"""Кошик покупок."""

from .products import get_product


def add_to_cart(product_id: int) -> list[dict[str, int | str]]:
    """Додає товар до кошика та повертає список товарів."""
    return [get_product(product_id)]
