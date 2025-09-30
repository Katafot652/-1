nums = input("Enter numbers separeted by space: ").split()
nums = [int(x) for x in nums]

for n in nums:
    result = ((-15 < n <= 12) or (14 < n < 17) or (n >= 19))
    print(n, "->", result)