### `min()` і `max()`

python

```python
nums = [5, 2, 9, 1]

min(nums)              # 1
max(nums)              # 9
min(3, 7, 2)           # 2  (можна передати значення напряму)
max("python")          # 'y'  (порівнюються символи)
```

**`key`**: за яким критерієм порівнювати

python

```python
words = ["кіт", "банан", "я"]
max(words, key=len)                    # 'банан'
min(words, key=len)                    # 'я'

people = [("Оля", 25), ("Іван", 20)]
max(people, key=lambda p: p[1])        # ('Оля', 25)
```

**`default`**: значення для порожньої колекції

python

```python
min([])                  # ValueError
min([], default=0)       # 0
```

**Словник**

python

```python
d = {"a": 3, "b": 1, "c": 2}
max(d)                   # 'c'  (за ключем)
max(d, key=d.get)        # 'a'  (ключ з найбільшим значенням)
max(d.values())          # 3
```

### `sum()`

python

```python
sum([1, 2, 3])                  # 6
sum([1, 2, 3], 10)              # 16  (початкове значення, за замовчуванням 0)
sum(x * 2 for x in [1, 2, 3])   # 12  (з генератором)
sum([0.1, 0.2, 0.3])            # 0.6000000000000001 (похибка float)
sum(["a", "b"])                 # TypeError: для рядків використовуйте "".join()
```

**Корисний трюк**: `True` це 1, а `False` це 0, тому `sum` рахує, скільки елементів підходять:

python

```python
sum(x > 2 for x in [1, 2, 3, 4])   # 2
```

### `all()`

Повертає `True`, якщо **всі** елементи істинні (логічне «І»).

python

```python
all([True, True, True])            # True
all([True, False, True])           # False
all([])                            # True  (для порожньої колекції завжди True)
all(x > 0 for x in [1, 2, 3])      # True
all("abc")                         # True (усі символи непорожні)
```

### `any()`

Повертає `True`, якщо **хоча б один** елемент істинний (логічне «АБО»).

python

```python
any([False, False, True])          # True
any([False, False])                # False
any([])                            # False  (для порожньої колекції завжди False)
any(x > 3 for x in [1, 2, 5])      # True
```

### Що вважається `False`

`False`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()`, `None`. Усе інше це `True`.

python

```python
any([0, "", None])        # False
all([1, "a", [0]])        # True ([0] не порожній список)
```

### Типові задачі

python

```python
s = "abc123"
any(c.isdigit() for c in s)       # True, є цифра
all(c.isalpha() for c in s)       # False, не всі літери

lst = [3, 8, 1]
all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))   # чи відсортований
sum(1 for x in lst if x > 2)                              # кількість підходящих
```

### Підсумок

|Функція|Що повертає|Для порожньої колекції|
|---|---|---|
|`min`|найменший елемент|`ValueError` (або `default`)|
|`max`|найбільший елемент|`ValueError` (або `default`)|
|`sum`|сума|`0`|
|`all`|`True`, якщо всі істинні|`True`|
|`any`|`True`, якщо є хоч один істинний|`False`|

Можу додати ці функції в `.py` файл, як у попередніх.