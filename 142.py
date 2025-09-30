nums = input("Enter the number of sides (separated by space): ").split()

nums = [int(x) for x in nums]

for n in nums:
    if n == 3:
        print("That's a triangle.")
    elif n == 4:
        print("That's a quadrilateral.")
    elif n == 5:
        print("That's a pentagon.")
    elif n == 6:
        print("That's a hexagon.")
    else:
        print("That number of sides is not supported by this program.")