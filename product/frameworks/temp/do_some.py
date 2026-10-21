def do_some(name: str) -> None:
    print(name, " do some thing")

def do_some_2(name: str) -> str:
    return f"{name} do some thing"

print(do_some_2("John"))
