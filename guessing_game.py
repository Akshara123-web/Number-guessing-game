import random

print("🎯 Welcome to the Number Guessing Game!")

# Take range input
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

# Generate random number
number = random.randint(lower, upper)

attempts = 0

print(f"\nI have chosen a number between {lower} and {upper}. Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break

    elif guess < number:
        print("📉 Too low!")

        if number - guess <= 5:
            print("🔥 Very close! Just a bit higher.")
        elif number - guess <= 10:
            print("🙂 Getting closer!")

    else:
        print("📈 Too high!")

        if guess - number <= 5:
            print("🔥 Very close! Just a bit lower.")
        elif guess - number <= 10:
            print("🙂 Getting closer!")