# `*args` та `**kwargs`
### Приклад повної функції

```python
def describe_event(event_name, *participants, location="Онлайн", **details):
    print(f"Подія: {event_name}")
    print(f"Локація: {location}")
    
    print("Учасники:")
    for person in participants:
        print(f"- {person}")
        
    if details:
        print("Деталі:")
        for key, value in details.items():
            print(f"  {key}: {value}")

# Виклик функції
describe_event(
    "Python Meetup", 
    "Олег", "Марія", "Іван", 
    location="Київ", 
    topic="Веб-розробка", 
    duration="2 години"
)
```
