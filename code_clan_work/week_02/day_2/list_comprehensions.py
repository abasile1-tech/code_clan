numbers = range(1, 11)
print([number for number in numbers if number % 2 == 0])

# Take a list of numbers
# and output a list with "Even"
# if number is even and "Odd" if the number is odd
# ["Odd","Even","Odd"]

print(["Even" if number % 2 == 0 else "Odd" for number in numbers])