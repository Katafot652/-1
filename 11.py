#read data (three examoles of conditions
n1 = float (input("Введіть значення №1 "))
n2 = float (input("Введіть значення №2 "))
n3 = float (input("Введіть значення №3 "))

# Calculation for each bill
p1 = int(n1 / 10)
p2 = int(n2 / 10)
p3 = int(n3 / 10)

# Output results (rounding to 2 demical places)
print(f"Значення №1: {p1} десятків")
print(f"Значення №2: {p2} десятків")
print(f"Значення №3: {p3} десятків")