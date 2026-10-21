class_register = {
  "Robb Stark": 2,
  "Sansa Stark": 12,
  "Arya Stark": 2,
  "Bran Stark": 2,
  "Jon Snow": 2,
}


def get_unique_marks(class_register: dict) -> list:
    # write your code here
    print(f"val:  {set(class_register.values())}")
    return list(set(class_register.values()))
    pass

print(f"res:  {get_unique_marks(class_register)}")