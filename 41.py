#first, store the 3 numbers in a list
numbers = [float(input("Enter a number: ")) for _ in range(3)]

#Then, print results
for n in numbers:
    print(int(n))