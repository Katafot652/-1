nums = input("Enter numbers separeted by space: ").split()

nums = [int(x) for x in nums]

for n in nums:
    if 10 <= n <= 99:
        print(n, "-> True ")
    else:
        print(n, "-> False ")