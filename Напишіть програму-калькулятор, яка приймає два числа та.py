# Введення даних
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

# Обчислення
sum_res = a + b
diff_res = a - b
prod_res = a * b

# Виведення результатів
print(f"Сума: {sum_res}")
print(f"Різниця: {diff_res}")
print(f"Добуток: {prod_res}")

# Перевірка ділення на нуль
if b != 0:
    div_res = a / b
    print(f"Частка: {div_res}")
else:
    print("Частка: Помилка! Ділення на нуль неможливе.")
