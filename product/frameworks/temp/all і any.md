`all` і `any` перевіряють, чи виконується умова для елементів колекції. Результат завжди `True` або `False`.

- **`all()`**: чи виконується умова для **всіх** елементів («усі»)
- **`any()`**: чи виконується умова **хоча б для одного** елемента («хоч якийсь»)

### Простий приклад

Уявіть, що є оцінки студентів:

python

```python
marks = [80, 90, 45, 70]

all(m >= 50 for m in marks)   # False: не всі склали (45 менше 50)
any(m >= 50 for m in marks)   # True: хоча б хтось склав
```

Тут `m >= 50 for m in marks` створює послідовність `True/False` для кожної оцінки:

```
[True, True, False, True]
```

- `all` дивиться: чи всі `True`? Ні, є `False`, тому результат `False`.
- `any` дивиться: чи є хоч один `True`? Так, тому результат `True`.

### Те саме без `all` / `any`

python

```python
# all
result = True
for m in marks:
    if not m >= 50:
        result = False
        break

# any
result = False
for m in marks:
    if m >= 50:
        result = True
        break
```

`all` і `any` замінюють такі цикли одним рядком.

### Де це корисно

python

```python
password = "abc123"

any(c.isdigit() for c in password)    # True: є хоча б одна цифра
all(c.isalpha() for c in password)    # False: не всі символи літери

"x" in "abc"                          # перевірка одного значення
any(w in text for w in ["a", "b"])    # чи є хоч одне зі слів у тексті
```

### Важливі моменти

Вони зупиняються одразу, як відомий результат:

- `all` зупиняється на першому `False`
- `any` зупиняється на першому `True`

python

```python
all([])   # True   (порожня колекція: немає елементів, які б порушили умову)
any([])   # False  (порожня колекція: немає жодного підходящого)
```

Можна запам'ятати так: `all` це «І» між усіма елементами, а `any` це «АБО» між усіма елементами.

python

```python
all([a, b, c])  ==  a and b and c
any([a, b, c])  ==  a or b or c
```