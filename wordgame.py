import random
import os

#todo - data checking for every input

guessBalance = 5 #default guesses allowed
target = [] #empty list to be appended with target word in word() and referenced throughout code
length = 5 #default length of word

print("\nWelcome to Storts, Chophy, Bascat!\n"
          "Your objective is to guess the correct word.\n"
          "You have 5 guesses total. Good luck!\n")

def main():

    menu = (input("[MENU]: \n"
                  "[1] Play Game\n"
                  "[2] Adjust Difficulty\n"
                  "[3] Exit\n"
                  "\nYour Choice: "))

    if menu == "1":
        clear()  # clear os
        word()  # create target
        print("\n STORTS CHOPHY BASCAT")
        print("\nWord Length: ", length)
        game()  # start game
    elif menu == "2":
        clear()  # clear os
        difficulty()  # adjust difficulty
        game()  # run game once difficulty is adjusted
    elif menu == "3":
        print("\n Exiting...")
        exit()
    else:
        clear()
        input("\n [!] Invalid  Input!\n"
              "[*] Must be 1, 2, or 3!\n"
              "Press Enter to Continue...")
        clear()
        main()

def game():
    global guessBalance
    print("\nGuesses Left: " , guessBalance)
    print("Word Length: ", length)

    guess = str(input("Guess a word!: "))

    if guess == target:
        print("Correct! You guessed the word!")
        gameOver()
    elif len(guess) == len(target):
        guessBalance -= 1
        if guessBalance == 0:
            gameOver()
        #splits guess and target into characters
        splitGuess = list(guess)
        splitTarget = list(target)
        #compares each index in both lists
        #todo - append what is printed into a list split by \n per print so that it can be printed whenever clear()
        for x in range(length):
            if splitGuess[x] == splitTarget[x]:
                print("Chophy - " , splitGuess[x])
            else:
                if splitGuess[x] in splitTarget:
                    print("Storts - " , splitGuess[x])
                else:
                    print("Bascat - " , splitGuess[x])
    else:
        #todo - fix data checking
        clear()
        print("\n [!] Invalid  Input: Follow These Conditions...\n"
              "[*] Must be " , length , " letters long.\n"
              "[*] Must be letters, not numbers.\n"
              "Click enter to continue...")
        input()
        clear()
    game() #todo - make call non self-referential

def word():
    # english dictionary, target word w/ given length is pulled from here
    global target
    dictionary = []
    with open("assets/words_alpha.txt", "r") as file:
        english = file.read().split('\n')
        for words in english:
            #appends all words with desired length into the dictionary
            if len(words) == length:
                dictionary.append(words)
    target = dictionary[random.randint(0, len(dictionary) - 1)]

def difficulty():
    clear()
    global guessBalance
    global length
    try:
        length = int(input("Choose word length: "))
        if length <= 0:
            clear()
            input("\n [!] Invalid Input: Must be positive integer.\n"
                  "Press Enter to Continue...")
            difficulty()
    except ValueError:
        clear()
        input("[!] Invalid Input! \n"
          "[1] Input must be an integer\n"
          "[2] Input must be greater than 0\n"
              "Click enter to continue...")
        difficulty()
    try:
        guessBalance = int(input("Choose guess amount: ")) #referenced in game()
        if guessBalance <= 0:
            input("\n [!] Invalid Input: Must be positive integer.\n"
                  "Press Enter to Continue...")
            difficulty()
    except ValueError:
        try:
            length = int(input("Choose word length: "))  # this is referenced in word()
        except ValueError:
            clear()
            input("[!] Invalid Input! \n"
                  "[1] Input must be an integer\n"
                  "[2] Input must be greater than 0\n"
                  "Click enter to continue...")
            difficulty()
    word()
    clear()

def gameOver():
    clear()
    print("\n[!] Game Over!\n"
          "The word was: " , target,
          "\n \n Play Again?\n")
    input("Press Enter to Continue...")
    if input:
        main()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


main()
