import sys
import random

# Ensure correct number of arguments
if len(sys.argv) != 3:
    print("Error: Incorrect number of arguments.")
    sys.exit(1)

# Read input values
try:
    number = int(sys.argv[1])
    text = sys.argv[2]
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

# Task 1: Number Puzzle
if number % 2 == 0:
    number_result = f"The number {number} is even. Its square root is {number ** 0.5:.2f}."
else:
    number_result = f"The number {number} is odd. Its cube is {number ** 3}."

# Task 2: Text Puzzle
binary_text = ' '.join(format(ord(char), '08b') for char in text)
vowel_count = sum(1 for char in text.lower() if char in "aeiou")

text_result = f"Binary representation of '{text}': {binary_text}\nNumber of vowels: {vowel_count}"

# Task 3: Treasure Hunt
secret_number = random.randint(1, 100)
attempts = 0
found = False

while attempts < 5:
    guess = random.randint(1, 100)  # Simulated guesses
    attempts += 1
    if guess == secret_number:
        found = True
        break

treasure_result = "Congratulations! You found the treasure!" if found else f"Sorry! The treasure was {secret_number}."

# Print the results for PHP to display
print(number_result)
print(text_result)
print(treasure_result)
