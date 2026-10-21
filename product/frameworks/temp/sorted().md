Сигнатура: `sorted(iterable, *, key=None, reverse=False)`

### 1. Базове сортування

python

```python
sorted([3, 1, 2])          # [1, 2, 3]
sorted("python")           # ['h', 'n', 'o', 'p', 't', 'y']  (повертає список символів)
sorted((3, 1, 2))          # [1, 2, 3]  (кортеж, результат все одно список)
sorted({3, 1, 2})          # [1, 2, 3]  (множина)
```

### 2. `reverse`: у зворотному порядку

python

```python
sorted([3, 1, 2], reverse=True)    # [3, 2, 1]
```

### 3. `key`: за яким критерієм сортувати

python

```python
words = ["банан", "я", "яблуко", "кіт"]

sorted(words, key=len)                    # за довжиною
sorted(words, key=str.lower)              # без урахування регістру
sorted(words, key=lambda w: w[-1])        # за останньою літерою
sorted(words, key=len, reverse=True)      # довгі спочатку
```

### 4. Сортування словника

python

```python
d = {"a": 3, "b": 1, "c": 2}

sorted(d)                                  # ['a', 'b', 'c'] (ключі)
sorted(d.keys())                           # те саме
sorted(d.values())                         # [1, 2, 3]
sorted(d.items())                          # за ключем: [('a', 3), ('b', 1), ('c', 2)]
sorted(d.items(), key=lambda x: x[1])      # за значенням
dict(sorted(d.items(), key=lambda x: x[1]))   # знову словник
```

### 5. Список кортежів / списків (за конкретним полем)

python

```python
people = [("Оля", 25), ("Іван", 20), ("Петро", 30)]

sorted(people)                                   # за першим елементом
sorted(people, key=lambda p: p[1])               # за віком
sorted(people, key=lambda p: p[1], reverse=True)
```

### 6. `itemgetter` і `attrgetter` (швидше за lambda)

python

```python
from operator import itemgetter, attrgetter

sorted(people, key=itemgetter(1))        # за індексом 1

class User:
    def __init__(self, name, age):
        self.name, self.age = name, age

users = [User("Оля", 25), User("Іван", 20)]
sorted(users, key=attrgetter("age"))     # за атрибутом
```

### 7. Сортування за кількома критеріями

python

```python
data = [("Оля", 25), ("Іван", 25), ("Петро", 20)]

sorted(data, key=lambda x: (x[1], x[0]))      # спочатку вік, потім ім'я
sorted(data, key=lambda x: (-x[1], x[0]))     # вік за спаданням, ім'я за зростанням
sorted(data, key=itemgetter(1, 0))            # те саме через itemgetter
```

Мінус перед числом дає зворотний порядок лише для цього поля.

### 8. Сортування рядків-чисел

python

```python
nums = ["10", "9", "2"]

sorted(nums)                  # ['10', '2', '9']  (як рядки, не те, що треба)
sorted(nums, key=int)         # ['2', '9', '10']
```

### 9. Регістр і спецсимволи

python

```python
sorted(["b", "A", "a", "B"])                     # ['A', 'B', 'a', 'b']  (великі перед малими)
sorted(["b", "A", "a", "B"], key=str.lower)      # ['A', 'a', 'b', 'B']  (за алфавітом)
```

### 10. Стабільність сортування

`sorted` стабільний: елементи з однаковим ключем зберігають початковий порядок. Тому можна сортувати у два проходи:

python

```python
data = sorted(data, key=lambda x: x[0])    # спочатку за ім'ям
data = sorted(data, key=lambda x: x[1])    # потім за віком (імена в межах віку залишаться відсортованими)
```

### Відмінність від `list.sort()`

||`sorted(x)`|`x.sort()`|
|---|---|---|
|Що повертає|новий список|`None`|
|Змінює оригінал|ні|так|
|Працює з|будь-яким ітерованим|лише зі списками|
|Параметри|`key`, `reverse`|`key`, `reverse`|

python

```python
lst = [3, 1, 2]
lst.sort()                  # lst тепер [1, 2, 3]
x = lst.sort()              # x == None (типова помилка)
```

```python  
def weekday_order(weekday: str) -> int:  
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  
    return days.index(weekday)  
  
  
def sort_weekdays(weekdays: list) -> list:  
    return sorted(weekdays, key=weekday_order)  
  
  
# Приклади з тестовими даними:  
if __name__ == "__main__":  
    print(sort_weekdays(["Monday"]))  
    # Результат: ['Monday']  
  
    print(sort_weekdays(["Saturday", "Wednesday"]))  
    # Результат: ['Wednesday', 'Saturday']  
  
    print(sort_weekdays(["Sunday", "Tuesday", "Thursday", "Monday"]))  
    # Результат: ['Monday', 'Tuesday', 'Thursday', 'Sunday']
```