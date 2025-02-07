import sys
import random

# Validación de argumentos
if len(sys.argv) != 3:
    print("Error: Incorrect number of arguments.")
    sys.exit(1)

# Leer y validar entrada
try:
    number = int(sys.argv[1])
    text = sys.argv[2]
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

# **Task 1: Number Puzzle**
if number % 2 == 0:
    number_result = f"- The number {number} is even. Its square root is {number ** 0.5:.2f}."
else:
    number_result = f"- The number {number} is odd. Its cube is {number ** 3}."

# **Task 2: Text Puzzle**
binary_text = ' '.join(format(ord(char), '08b') for char in text)
vowel_count = sum(1 for char in text.lower() if char in "aeiou")

text_result = f"- Binary: {binary_text}\n- Vowel Count: {vowel_count}"

# **Task 3: Treasure Hunt**
secret_number = random.randint(1, 100)
attempts = 0
found = False
guess_history = []

while attempts < 5:
    guess = random.randint(1, 100)  # Simular un intento
    attempts += 1

    if guess > secret_number:
        guess_history.append(f"- Attempt {attempts}: {guess} (Too high!)")
    elif guess < secret_number:
        guess_history.append(f"- Attempt {attempts}: {guess} (Too low!)")
    else:
        guess_history.append(f"- Attempt {attempts}: {guess} (Correct!)")
        found = True
        break

treasure_result = f"- The secret number is {secret_number}.\n" + "\n".join(guess_history)
if found:
    treasure_result += f"\n- You found the treasure in {attempts} attempts!"
else:
    treasure_result += "\n- You ran out of attempts! Better luck next time."

# **Mostrar resultados**
print("Number Puzzle:")
print(number_result, "\n")
print("Text Puzzle:")
print(text_result, "\n")
print("Treasure Hunt:")
print(treasure_result)
