# Объединённые типы в Python (Union Types)

Аннотации типов подсказывают, какие данные ожидает функция. Python их **не проверяет** во время выполнения: их читают редакторы (PyCharm, VS Code) и проверяющие утилиты (`mypy`). Они делают код понятнее и помогают находить ошибки до запуска.

## Краткая таблица

| Тип | Что значит | Когда использовать |
|---|---|---|
| `A \| B` / `Union[A, B]` | значение типа A **или** B | параметр может быть числом или строкой |
| `Optional[A]` / `A \| None` | значение типа A **или** `None` | значения может не быть |
| `Any` | любой тип | тип заранее неизвестен или не важен |
| `Literal["a", "b"]` | только перечисленные значения | допустим ограниченный набор значений |
| `@overload` | разные сигнатуры для разных типов | тип результата зависит от типа аргумента |
| `TypeVar` | «тот же тип, что на входе» | функция работает с любым типом и возвращает его же |

---

## 1. `|` и `Union`: «или»

Значение может быть одного из нескольких типов. Оператор `|` работает с Python 3.10, до этого использовали `Union`.

**Когда:** данные приходят в разных видах, например число как `5` или как `"5"`.

```python
from typing import Union

def get_winner(max_solved: str | int, roman_solved: str | int) -> str:
    m = int(max_solved)       # приводим к одному типу
    r = int(roman_solved)

    if m > r:
        return "Max winner!!!"
    elif r > m:
        return "Roman winner!!!"
    return "Roman and Maxim are the winners!!!"

# старый способ (до 3.10)
def old_style(value: Union[str, int]) -> str:
    return str(value)
```

Можно перечислять сколько нужно типов:

```python
def to_number(value: int | float | str) -> float:
    return float(value)
```

## 2. `Optional`: значение или `None`

`Optional[str]` то же самое, что `str | None`.

**Когда:** параметр необязательный, или функция может ничего не найти и вернуть `None`.

```python
from typing import Optional

def find_user(name: Optional[str] = None) -> str | None:
    if name is None:
        return None
    return name.title()
```

## 3. `Any`: любой тип

Отключает проверку типа для этого значения.

**Когда:** тип действительно может быть любым (например, функция просто выводит значение) или вы временно не хотите описывать тип. Использовать стоит редко, потому что теряется польза от подсказок.

```python
from typing import Any

def show(value: Any) -> None:
    print(value)
```

## 4. `Literal`: только конкретные значения

Ограничивает не тип, а сами допустимые значения.

**Когда:** параметр принимает фиксированный набор вариантов: режим, статус, направление.

```python
from typing import Literal

def set_mode(mode: Literal["easy", "hard"]) -> None:
    print(mode)

set_mode("easy")     # ок
set_mode("medium")   # редактор подсветит ошибку
```

## 5. `isinstance`: проверка типа внутри функции

Это не аннотация, а проверка во время выполнения. Она нужна, когда с `A | B` нужно работать по-разному.

**Когда:** после `str | int` логика зависит от того, что именно пришло.

```python
def process(value: str | int) -> str:
    if isinstance(value, int):
        return f"Число: {value}"
    return f"Строка: {value}"

isinstance(value, (int, float))   # проверка на несколько типов сразу
```

## 6. `@overload`: разные типы на входе и на выходе

Описывает, что результат зависит от типа аргумента: int на входе даёт int, str даёт str.

**Когда:** одна функция работает с разными типами, и нужно точно описать, что она вернёт. Нужен в основном при написании библиотек.

```python
from typing import overload

@overload
def double(x: int) -> int: ...
@overload
def double(x: str) -> str: ...

def double(x):
    return x * 2
```

## 7. `TypeVar`: обобщённые типы

Переменная типа: «что зашло, того же типа и вышло».

**Когда:** универсальная функция работает с любым типом данных и возвращает значение того же типа.

```python
from typing import TypeVar

T = TypeVar("T")

def first_item(items: list[T]) -> T:
    return items[0]

first_item([1, 2, 3])        # int
first_item(["a", "b"])       # str
```

---

## Важно помнить

- Аннотации не защищают от ошибок во время выполнения: `get_winner([1], {})` запустится и упадёт уже на `int(...)`.
- `int("abc")` вызовет `ValueError`. Для безопасности можно использовать `.isnumeric()` или `try/except`.
- Для начала достаточно `|` и `Optional`. Остальное нужно реже.
