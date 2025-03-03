#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Get the last digit (handling negative numbers correctly)
last_digit = abs(number) % 10 if number >= 0 else -(abs(number) % 10)

# Print the output as per the requirements
print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
