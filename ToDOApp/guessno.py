import random

number = random.randint(1, 10)
count = 0
attempts = 5

while attempts > 0:
    guess = int(input("Guess the Number: "))

    diff = abs(guess - number)
    count += 1
    attempts -= 1

    if guess > 10:
        print("Please enter Btw 1 to 10", end=" ")

    if guess == number:
        print(f"Yavy!!, Your Guess is right the number is {number}")
        break
    elif guess > number:
        print(f"Guess was too high")
    elif diff <= 3:
        print(f"Your Close")
    else:
        print(f"To Low guess")

        if attempts == 0 and guess != number:
            print(f"Attempts exceeded Number was {number}")

print(f"Total Attempts took to guess {count}")
