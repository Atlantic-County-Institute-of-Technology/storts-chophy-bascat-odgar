import random
import os

# storts_chophy_bascat.py
# description: A word-guessing game where players guess a target word based on feedback.
# code by oscar euceda
# created november 2025

# yes there is excessive comments on here. it's for my own clarity.


def main():
    while True:
        print("\nWelcome to Storts, Chophy, Bascat!\n"
              "Your objective is to guess the correct word.\n"
              "You have 5 guesses total. Good luck!\n")

        menu = input("[MENU]: \n"
                     "[1] Play Game\n"
                     "[2] Adjust Difficulty\n"
                     "[3] Exit\n"
                     "\nYour Choice: ")

        if menu == "1":
            clear()
            guessBalance, length = 5, 5  #default values if none are selected via option 2
            target = word(length) #target is defined in word function, which uses predefined
            print("\n STORTS CHOPHY BASCAT")
            print("\nWord Length: ", length)
            game(target, guessBalance, length) #target is a word of length 5, guessBalance is 5, and length is 5
        elif menu == "2":
            clear()
            guessBalance, length = difficulty() #both guessBalance and length are defined by the user via the difficulty function
            target = word(length) #target is defined in word function, which uses length defined in difficulty function
            game(target, guessBalance, length) #runs game function with these new parameters
        elif menu == "3":
            print("\n Exiting...")
            exit()
        else:
            clear()
            input("\n [!] Invalid Input!\n"
                  "[*] Must be 1, 2, or 3!\n"
                  "Press Enter to Continue...")
            clear()

#guessBalance and length are either default values from main function or user-defined values from difficulty function
#target is defined in main function as well. remember that it is simply the returned string value from word function
def game(target, guessBalance, length):
    while True:
        print("\nGuesses Left: ", guessBalance)
        print("Word Length: ", length)

        guess = input("Guess a word!: ")

        if guess == target:
            print("Correct! You guessed the word!")
            gameOver(target)
            break
        elif len(guess) == len(target):
            guessBalance -= 1
            if guessBalance == 0:
                gameOver(target)
                break
            #this makes each variable into a list split by their characters and them compares them index by index
            splitGuess = list(guess)
            splitTarget = list(target)
            for x in range(length):
                if splitGuess[x] == splitTarget[x]:
                    print("Chophy - ", splitGuess[x])
                else:
                    if splitGuess[x] in splitTarget:
                        print("Storts - ", splitGuess[x])
                    else:
                        print("Bascat - ", splitGuess[x])
        else:
            clear()
            print("\n [!] Invalid Input: Follow These Conditions...\n"
                  "[*] Must be ", length, " letters long.\n"
                  "[*] Must be letters, not numbers.\n"
                  "Click enter to continue...")
            input()
            clear()

def word(length):
    dictionary = []
    with open("assets/words_alpha.txt", "r") as file:
        english = file.read().split('\n')
        for words in english:
            if len(words) == length:
                dictionary.append(words)
    return dictionary[random.randint(0, len(dictionary) - 1)]

def difficulty():
    while True:
        try:
            length = int(input("Choose word length: "))
            if length > 0:
                break
            else:
                clear()
                input("\n [!] Invalid Input: Must be positive integer.\n"
                      "Press Enter to Continue...")
        except ValueError:
            clear()
            input("[!] Invalid Input! \n"
                  "[1] Input must be an integer\n"
                  "[2] Input must be greater than 0\n"
                  "Click enter to continue...")

    while True:
        try:
            guessBalance = int(input("Choose guess amount: "))
            if guessBalance > 0:
                break
            else:
                input("\n [!] Invalid Input: Must be positive integer.\n"
                      "Press Enter to Continue...")
        except ValueError:
            clear()
            input("[!] Invalid Input! \n"
                  "[1] Input must be an integer\n"
                  "[2] Input must be greater than 0\n"
                  "Click enter to continue...")

    clear()
    return guessBalance, length

#game over function
#uses target as parameter to reveal correct word: referenced from game function
def gameOver(target):
    clear()
    print("\n[!] Game Over!\n"
          "The word was: ", target,
          "\n \n Play Again?\n")
    input("Press Enter to Continue...")
    main()

#clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


main()
