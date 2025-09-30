nums = input("Enter the number of sides (separated by space): ").split()

nums = [int(x) for x in nums]

nums.sort()

product = nums[0] * nums[1]

print(product)