# Read three numbers (each on a new line)
numbers = [int(input("Enter a number of seconds: ")) for _ in range(3)]

# Process each number
for seconds in numbers:
    days = seconds // 86400
    seconds = seconds % 86400

    hours = seconds // 3600
    seconds = seconds % 3600

    minutes = seconds // 60
    seconds = seconds % 60

    print(f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s).")