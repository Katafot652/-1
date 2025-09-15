# Програма для знаходження першої цифри після десяткової крапки

# Ввід трьох чисел (кожне окремо)
a1 = float(input("Enter the first positive real number: "))
a2 = float(input("Enter the second positive real number: "))
a3 = float(input("Enter the third positive real number: "))

# Обчислення першої цифри після десяткової крапки
digit1 = int(a1 * 10) % 10
digit2 = int(a2 * 10) % 10
digit3 = int(a3 * 10) % 10

# Вивід результатів
print("The first digit after the decimal point in", a1, "is:", digit1)
print("The first digit after the decimal point in", a2, "is:", digit2)
print("The first digit after the decimal point in", a3, "is:", digit3)

# Кінець програми
print("Program finished.")