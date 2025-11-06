name = input().strip()
if not name:
    raise Exception("Некорректное имя")
else:
    print("Имя введено корректно")

age = int(input())
if age < 0 or age > 120:
    raise Exception("Некорректный возраст")
else:
    print("Возраст введен корректно")

gender = input()
assert gender in ['м', 'ж'], "Некорректный пол"
print("Пол введен корректно")
