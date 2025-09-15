# Input from the user
feet = float(input("Input distance in feet: "))

# Conversions
inches = feet * 12
yards = feet * 0.333333333
miles = feet * 0.000189393939

# Output results
print(f"The distance in inches is {inches:.0f} inches.")
print(f"The distance in yards is {yards:.3f} yards.")
print(f"The distance in miles is {miles:.3f} miles.")