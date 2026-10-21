Я припускаю, що йдеться про модуль `random` у Python.

`random` генерує псевдовипадкові числа та вибирає випадкові елементи. Числа обчислюються за алгоритмом (Mersenne Twister), тому вони не справжні випадкові. Для паролів і токенів його використовувати не можна, для цього є модуль `secrets`.

python

```python
import random
```

### Числа

python

```python
random.random()            # float від 0.0 до 1.0 (1.0 не входить)
random.uniform(1, 10)      # float від 1 до 10
random.randint(1, 6)       # ціле від 1 до 6 (обидва кінці входять)
random.randrange(0, 10, 2) # ціле з range: 0, 2, 4, 6, 8
random.gauss(0, 1)         # нормальний розподіл (середнє, відхилення)
```

### Вибір з колекції

python

```python
items = ["a", "b", "c", "d"]

random.choice(items)                  # один елемент
random.choices(items, k=3)            # 3 елементи, можливі повтори
random.choices(items, weights=[5, 1, 1, 1], k=3)   # з вагами (імовірностями)
random.sample(items, 2)               # 2 унікальні елементи, без повторів
```

### Перемішування

python

```python
random.shuffle(items)                 # перемішує список на місці, повертає None
shuffled = random.sample(items, len(items))   # новий перемішаний список
```

### Відтворюваність (seed)

python

```python
random.seed(42)
print(random.randint(1, 100))   # з однаковим seed завжди буде той самий результат
```

Це корисно для тестів і налагодження.

### Інше

python

```python
random.getrandbits(8)         # випадкові біти (число від 0 до 255)
random.randbytes(4)           # випадкові байти (Python 3.9+)
random.getstate()             # зберегти внутрішній стан генератора
random.setstate(state)        # відновити стан
r = random.Random(123)        # окремий генератор зі своїм seed
```

### Типові помилки

- `randint(a, b)` включає **обидва** кінці, а `randrange(a, b)` не включає `b`.
- `random.shuffle()` повертає `None`, тому запис `x = random.shuffle(lst)` не спрацює.
- `random.sample()` не працює з множинами в нових версіях Python, спершу перетворіть їх на список або кортеж.
- Для криптографії використовуйте `secrets.token_hex()`, `secrets.choice()`.

Якщо потрібно, можу оформити це у вигляді `.py` файлу з окремою функцією на кожен метод, як у попередньому.