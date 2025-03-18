"# Number_Guessing_Game" 

def gameplay(secret_num, a, b, guess_limit = 5):
    guess_count = 0
    guess_count_2 = 5
    while guess_count < guess_limit:
        try:
            guess_num = int(input(f"Guess the number from {a} to {b}: "))
            guess_count = guess_count + 1
            if guess_num > secret_num:
                print("Lower!")
            elif guess_num < secret_num:
                print("Higher!")
            elif guess_num == secret_num:
                print("You Win. Yeahhhhhhhh")
                print(f"Total guesses: {guess_count}")
                break
        except ValueError:
            print("Invalid! Please try again!!")
    else:
        print("YOU LOSEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        print(f"The correct number is {secret_num}")

def custom_game_play():
    while True:
        try:
            first_number = int(input("Enter your first number: "))
            last_number = int(input("Enter your last number: "))
            if first_number > last_number:
                print("First number must < last number. Please try again.")
                continue
            return first_number, last_number
        except ValueError:
            print("Invalid Input! Try again.")

import random

print("Welcome to the guessing game :D")

while True:
    print(( "1. Easy (1 - 20, 5 guesses)\n"
            "2. Medium (1 - 50, 5 guesses)\n"
            "3. Hardcore (1 - 100, 5 guesses)\n"
            "4. Custom\n"
            "5. Exit"))
    level_difficult = input("Choose difficulty: ")


    if level_difficult == "1":
        gameplay(random.randint(1, 20), 1, 20)

    elif level_difficult == "2":
        gameplay(random.randint(1, 50), 1, 50)

    elif level_difficult == "3":
        gameplay(random.randint(1, 20), 1, 50)

    elif level_difficult == "4":
        a, b = custom_game_play()
        while True:
            try:
                guess_limit_custom = int(input("Enter how many times you wanna guesses: "))
                if guess_limit_custom <0:
                    print("Guess limit must be > 0! Please Try Again.")
                    continue
                break
            except ValueError:
                print("Invalid! Please try again!!")
        gameplay(random.randint(a, b), a, b, guess_limit_custom)


    elif level_difficult == "5":
        print("Thank you and good bye")
        break

    else:
        print("Invalid! Must be from 1 to 5.")
