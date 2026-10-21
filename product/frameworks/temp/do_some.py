def do_some(name: str) -> None:
    print(name, " do some thing")

def do_some_2(name: str) -> str:
    return f"{name} do some thing"

print(do_some_2("John"))



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