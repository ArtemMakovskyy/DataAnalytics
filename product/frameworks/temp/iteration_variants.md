### 1. `for` по елементах (аналог for-each)

python

```python
nums = [10, 20, 30]
for x in nums:
    print(x)
```

Працює з будь-яким ітерованим об'єктом: список, кортеж, рядок, множина, словник, файл, генератор.

### 2. `for` з `range` (аналог класичного for з індексом)

python

```python
for i in range(5):            # 0..4
    print(i)

for i in range(2, 10, 3):     # 2, 5, 8 (початок, кінець, крок)
    print(i)

for i in range(10, 0, -1):    # у зворотному порядку
    print(i)
```

### 3. По індексах через `len`

python

```python
for i in range(len(nums)):
    print(i, nums[i])
```

Працює, але менш «пайтонівський», ніж `enumerate`.

### 4. `enumerate`: індекс і значення разом

python

```python
for i, x in enumerate(nums):
    print(i, x)

for i, x in enumerate(nums, start=1):   # нумерація з 1
    print(i, x)
```

### 5. `zip`: паралельний перебір кількох послідовностей

python

```python
names = ["Оля", "Іван"]
ages = [25, 30]
for n, a in zip(names, ages):
    print(n, a)

# zip_longest, якщо довжини різні
from itertools import zip_longest
for n, a in zip_longest(names, [1], fillvalue=None):
    print(n, a)
```

### 6. Перебір словника

python

```python
d = {"a": 1, "b": 2}

for k in d:                  # ключі
    print(k)
for k in d.keys():
    print(k)
for v in d.values():         # значення
    print(v)
for k, v in d.items():       # пари ключ-значення
    print(k, v)
```

### 7. `reversed` і `sorted`

python

```python
for x in reversed(nums):     # у зворотному порядку
    print(x)

for x in sorted(nums, reverse=True):   # відсортовано
    print(x)

for x in nums[::-1]:         # зріз з кроком -1
    print(x)
```

### 8. `while`

python

```python
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

while True:                  # нескінченний цикл з break
    line = input()
    if line == "q":
        break
```

Аналога `do-while` у Python немає. Його імітують так:

python

```python
while True:
    # тіло
    if not умова:
        break
```

### 9. `break`, `continue`, `else`

python

```python
for x in nums:
    if x == 20:
        continue      # пропустити ітерацію
    if x == 30:
        break         # вийти з циклу
    print(x)
else:
    print("Цикл завершився без break")   # унікальна фішка Python
```

Блок `else` виконується, лише якщо цикл не був перерваний через `break`. Працює і для `while`.

### 10. Вкладені цикли та `itertools.product`

python

```python
for i in range(3):
    for j in range(3):
        print(i, j)

# те саме одним циклом
from itertools import product
for i, j in product(range(3), repeat=2):
    print(i, j)
```

### 11. Comprehensions (генератори колекцій)

python

```python
squares = [x * x for x in nums]                 # список
evens   = [x for x in nums if x % 2 == 0]       # з фільтром
sq_set  = {x * x for x in nums}                 # множина
sq_dict = {x: x * x for x in nums}              # словник
gen     = (x * x for x in nums)                 # генератор (ліниво)
```

### 12. Функціональний стиль: `map`, `filter`, `reduce`

python

```python
list(map(lambda x: x * 2, nums))
list(filter(lambda x: x > 10, nums))

from functools import reduce
reduce(lambda a, b: a + b, nums)

# побічні ефекти (рідко, але можливо)
for _ in map(print, nums):
    pass
```

### 13. Ручна робота з ітератором: `iter` / `next`

python

```python
it = iter(nums)
print(next(it))              # 10
print(next(it, "кінець"))    # 20 (другий аргумент: значення за замовчуванням)

while True:
    try:
        x = next(it)
    except StopIteration:
        break
    print(x)
```

Саме так `for` працює «під капотом».

### 14. Генератори та власні ітератори

python

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)

# власний клас
class Counter:
    def __init__(self, n):
        self.n, self.i = n, 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i
```

### 15. Модуль `itertools` (корисні перебори)

python

```python
from itertools import (count, cycle, islice, chain, groupby,
                       permutations, combinations, takewhile, dropwhile)

for i in count(1):                      # 1, 2, 3, ... (нескінченно)
    if i > 3: break

for x in islice(cycle("AB"), 5):        # A B A B A
    print(x)

for x in chain([1, 2], [3, 4]):         # склеїти кілька послідовностей
    print(x)

for p in permutations([1, 2, 3]):       # перестановки
    print(p)
for c in combinations([1, 2, 3], 2):    # комбінації
    print(c)

for x in takewhile(lambda x: x < 3, [1, 2, 3, 1]):   # 1, 2
    print(x)
```

### 16. Перебір файлів і рядків

python

```python
with open("file.txt", encoding="utf-8") as f:
    for line in f:                      # лінива побудкова читання
        print(line.rstrip())

for ch in "привіт":                     # рядок по символах
    print(ch)

from pathlib import Path
for p in Path(".").glob("*.py"):        # файли в директорії
    print(p)
```

### 17. Розпакування в циклі

python

```python
pairs = [(1, "a"), (2, "b")]
for num, letter in pairs:
    print(num, letter)

for first, *rest in [(1, 2, 3), (4, 5, 6)]:
    print(first, rest)
```

### 18. Перебір з одночасною зміною колекції

python

```python
# безпечно: перебір копії
for x in nums[:]:
    if x == 20:
        nums.remove(x)

# або створити новий список
nums = [x for x in nums if x != 20]
```

Змінювати список під час перебору самого себе не варто, бо елементи можуть пропускатися.

### 19. `any`, `all`, `sum`, `min`, `max`: перебір без явного циклу

python

```python
any(x > 25 for x in nums)    # чи є хоч один
all(x > 5 for x in nums)     # чи всі
sum(x for x in nums)
max(nums, key=lambda x: -x)
```

### 20. Рекурсія та `while` зі стеком/чергою

python

```python
def walk(lst):
    for item in lst:
        if isinstance(item, list):
            walk(item)
        else:
            print(item)
```

---

#### Відповідність Java → Python

|Java|Python|
|---|---|
|`for (int i = 0; i < n; i++)`|`for i in range(n)`|
|`for (T x : list)`|`for x in list`|
|`list.forEach(...)`|`for x in list` / `map`|
|`Iterator<T> it`|`it = iter(...)` + `next(it)`|
|`stream().filter().map()`|comprehensions / `filter` / `map`|
|`do { } while (...)`|`while True: ... if not cond: break`|
|`Map.entrySet()`|`d.items()`|
|індекс + значення|`enumerate`|