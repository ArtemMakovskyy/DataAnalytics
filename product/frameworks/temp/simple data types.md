| Характеристика               | `list`                   | `tuple`      | `set`                               | `frozenset`            | `dict`                           |
| ---------------------------- | ------------------------ | ------------ | ----------------------------------- | ---------------------- | -------------------------------- |
| Тип                          | Список                   | Кортеж       | Множина                             | Незмінна множина       | Словник                          |
| Синтаксис                    | `[1, 2, 3]`              | `(1, 2, 3)`  | `{1, 2, 3}`                         | `frozenset({1, 2, 3})` | `{"key": "value"}`               |
| Зберігає порядок             | +                        | +            | −                                   | −                      | +                                |
| Допускає дублікати           | +                        | +            | −                                   | −                      | Ключі: −, значення: +            |
| Змінюваний                   | +                        | −            | +                                   | −                      | +                                |
| Доступ за індексом           | +                        | +            | −                                   | −                      | −                                |
| Доступ за ключем             | −                        | −            | −                                   | −                      | +                                |
| Пошук індексу `.index()`     | +                        | +            | −                                   | −                      | −                                |
| Перевірка `in`               | За значенням             | За значенням | За значенням                        | За значенням           | За ключем                        |
| Додавання елементів          | `.append()`, `.insert()` | −            | `.add()`, `.update()`               | −                      | `dict[key] = value`, `.update()` |
| Видалення елементів          | `.remove()`, `.pop()`    | −            | `.remove()`, `.discard()`, `.pop()` | −                      | `.pop()`, `.popitem()`           |
| Підрахунок `.count()`        | +                        | +            | −                                   | −                      | −                                |
| Сортування `.sort()`         | +                        | −            | −                                   | −                      | −                                |
| Об'єднання `.union()`        | −                        | −            | +                                   | +                      | −                                |
| Перетин `.intersection()`    | −                        | −            | +                                   | +                      | −                                |
| Використання як ключа `dict` | −                        | +*           | −                                   | +                      | −                                |

* `tuple` можна використовувати як ключ, лише якщо всі його елементи хешовані.

### Словник та варіанти перебору


### 1. `keys()` — ключі

python

```python
book = {"title": "Python Basics", "author": "Jane Doe", "year": 2024}

book.keys()             # dict_keys(['title', 'author', 'year'])
list(book.keys())       # ['title', 'author', 'year']

for key in book.keys():
    print(key)

for key in book:        # те саме: за замовчуванням перебираються ключі
    print(key)
```

### 2. `values()` — значення

python

```python
book.values()           # dict_values(['Python Basics', 'Jane Doe', 2024])
list(book.values())     # ['Python Basics', 'Jane Doe', 2024]

for value in book.values():
    print(value)
```

### 3. `items()` — пари ключ-значення

python

```python
book.items()            # dict_items([('title', 'Python Basics'), ...])

for key, value in book.items():
    print(f"{key}: {value}")
```

Приклад зі списком словників (книгарня):

python

```python
books = [
    {"title": "Python Basics", "author": "Jane Doe", "year": 2021},
    {"title": "Advanced Python", "author": "John Doe", "year": 2020},
]

for book in books:
    for key, value in book.items():
        print(f"{key}: {value}")
    print("----")
```

---
### Операції з множинами (`set`)

Множини можна об'єднувати, перетинати та порівнювати. Кожна операція має метод і оператор-скорочення, а результатом завжди є **нова множина** (оригінали не змінюються).

|Операція|Метод|Оператор|Що повертає|
|---|---|---|---|
|Об'єднання|`union()`|`\|`|усі елементи обох множин, без дублікатів|
|Перетин|`intersection()`|`&`|лише спільні елементи|
|Різниця|`difference()`|`-`|елементи з першої множини, яких немає в другій|
|Симетрична різниця|`symmetric_difference()`|`^`|елементи, що є лише в одній з множин|

python

```python
electronics = {"Alex", "Maria", "John"}
clothing = {"John", "Sophia", "Maria", "Mike"}

electronics.union(clothing)                 # або electronics | clothing
# {"Alex", "Maria", "John", "Sophia", "Mike"}  (усі клієнти)

electronics.intersection(clothing)          # або electronics & clothing
# {"John", "Maria"}  (були в обох відділах)

electronics.difference(clothing)            # або electronics - clothing
# {"Alex"}  (лише електроніка)

electronics.symmetric_difference(clothing)  # або electronics ^ clothing
# {"Alex", "Sophia", "Mike"}  (лише в одному з відділів)
```

Порядок має значення лише для різниці: `a - b` не дорівнює `b - a`. Для `|`, `&` та `^` порядок не важливий. Порожня множина створюється через `set()`, бо `{}` це порожній словник.