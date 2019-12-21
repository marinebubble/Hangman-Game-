
# time module, functions to work with time
import time

# to welcome the user
user_name = input("What is your name? ")

# to start
print ("Welcome to Hangman")
print ("Hello, " + user_name, "It's time to play!")

print(" ")
print(" ")

# time.sleep is to pause the time of execution
# in other words, to add delay

# wait for 1 second..
time.sleep(1)

# Start guessing
print("You can start guessing ..")
time.sleep(0.5)

# secret word to be guessed
word = "bear"

# creates a variable with empty value
guesses = ''

# the number of turns
turns = 5

# While loop for the turn
while turns > 0:

    # counter that starts with zero
    failed = 0

    # for every character in the secret word
    for char in word:
        if char in guesses:
            # print then out the character
            print (char)
        else:
            # if not found, print a dash
            print ("_")
            # and increase the failed counter
            failed += 1

    # if failed is equal to zero
    # because the it has no failed number increases
    # Winning the game
    if failed == 0:
        print("Congrats", user_name, "You WON!")
        # exit the script
        break

    print()


    # ask the user to guess a character
    guess = input("guess a SECRET word: ")

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:
        # turns counter decreases with 1 (now 9)
        turns -= 1

        # print wrong
        print ("Wrong ")
        print (" ")

        # how many turns are left
        print ("You have", +turns, "more guesses")

        # if the turns are equal to zero
        if turns == 0:
            print("Sorry MAN, you lose! ")




