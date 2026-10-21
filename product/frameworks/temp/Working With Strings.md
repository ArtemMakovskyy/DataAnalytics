Ось короткі приклади по темах з вашого уроку (Working With Strings):

### Special Symbols (спецсимволи)

python

```python
print("Рядок1\nРядок2")      # \n  новий рядок
print("Колонка1\tКолонка2")  # \t  табуляція
print("Він сказав: \"Привіт\"")  # \"  лапки
print("C:\\folder")          # \\  зворотний слеш
print(r"C:\new\text")        # r"" сирий рядок, символи не екрануються
```

### Strip (прибрати зайве з країв)

python

```python
s = "   привіт   "
s.strip()        # "привіт"
s.lstrip()       # "привіт   "  (зліва)
s.rstrip()       # "   привіт"  (справа)
"--hi--".strip("-")   # "hi"
```

### Count (підрахунок)

python

```python
"banana".count("a")      # 3
"banana".count("an")     # 2
"banana".count("a", 2)   # 2 (починаючи з індексу 2)
```

### Join (склеїти список у рядок)

python

```python
", ".join(["a", "b", "c"])   # "a, b, c"
"".join(["a", "b", "c"])     # "abc"
"\n".join(["один", "два"])   # по одному на рядок
```

Елементи мають бути рядками. Для чисел: `", ".join(map(str, [1, 2, 3]))`.

Протилежна операція — `split`:

python

```python
"a,b,c".split(",")   # ["a", "b", "c"]
```

### Slicing (зрізи)

python

```python
s = "Python"
s[0]       # "P"
s[-1]      # "n"
s[0:2]     # "Py"   (кінець не входить)
s[2:]      # "thon"
s[:3]      # "Pyt"
s[::2]     # "Pto"  (крок 2)
s[::-1]    # "nohtyP"  (розворот)
```

### Replace (заміна)

python

```python
"hello world".replace("o", "0")       # "hell0 w0rld"
"hello world".replace("o", "0", 1)    # "hell0 world" (лише перша)
"a b c".replace(" ", "")              # "abc"
```

Рядки незмінні, `replace` повертає новий рядок, а оригінал не змінюється.

### isnumeric / isalpha (перевірки)

python

```python
"123".isnumeric()    # True
"12.5".isnumeric()   # False (крапка не цифра)
"abc".isalpha()      # True
"abc1".isalpha()     # False
"abc1".isalnum()     # True (літери та цифри)
"123".isdigit()      # True
"   ".isspace()       # True
"hello".islower()    # True
"HELLO".isupper()    # True
```

### Бонус: часті методи для завдань уроку

python

```python
s = "Hello World"
s.upper()               # "HELLO WORLD"
s.lower()               # "hello world"
s.title()               # "Hello World"
s.capitalize()          # "Hello world"
s.startswith("He")      # True
s.endswith("ld")        # True
s.find("o")             # 4  (індекс, або -1 якщо немає)
s.index("o")            # 4  (помилка ValueError, якщо немає)
len(s)                  # 11
"@" in "a@b.com"        # True (для Valid Email)
f"Дякую, {s}!"          # f-рядок (для Thank You)
```