"""Товари магазину."""


def get_product(product_id: int) -> dict[str, int | str]:
    """Повертає товар за його ідентифікатором."""
    return {"id": product_id, "name": "Книга"}
