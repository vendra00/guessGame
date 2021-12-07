# Undefined Global Variables
SECRET_WORD: str
TRIES: int
SCORE: int = 0

# Defined Global Variables
IS_IN_THE_GUESS: int = 5
IS_NOT_IN_THE_GUESS: int = 10
WINNING_BONUS: int = 100
GAME_MODE_VALUE: int
EASY_MODE: int = 10
NORMAL_MODE: int = 7
HARD_MODE: int = 4


# Method that starts the match
def run():
    secret()
    game_mode()
    logos(1)
    play()


# Method that make a play in the game
def play():
    check(guess_word())


# Method that contains all messages outputs from the application
def logos(value):
    if value == 1:
        print("########################################")
        print("###          TIME TO PLAY            ###")
        print("########################################")
    elif value == 2:
        print("########################################")
        print("###    WELCOME TO GUESS THE WORD     ###")
        print("########################################")
    elif value == 3:
        print("########################################")
        print("###       SELECT A GAME MODE         ###")
        print("########################################")
        print("###       1 - EASY                   ###")
        print("###       2 - NORMAL                 ###")
        print("###       3 - HARD                   ###")
        print("########################################")
    elif value == 4:
        print("########################################")
        print("You will have : " + str(TRIES) + " attempts.\nGood Luck!")
        print("########################################")
    elif value == 5:
        print("########################################")
        print("You will have : " + str(TRIES) + " attempts.\nGood Luck!")
        print("########################################")
    elif value == 6:
        print("########################################")
        print("You will have : " + str(TRIES) + " attempts.\nGood Luck!")
        print("########################################")
    elif value == 7:
        print("########################################")
        print("No game mode with the given option!")
        print("########################################")
    elif value == 8:
        print("########################################")
        print("You Win!\nTotal Score: " + str(SCORE))
        print("########################################")
    elif value == 9:
        print("########################################")
        print("The word has this letters: ")
        print("########################################")
    elif value == 10:
        print("########################################")
        print("Keep Trying")
        print("########################################")
    elif value == 11:
        print("########################################")
        print("###   Do you want to play again?     ###")
        print("###   1 - YES                        ###")
        print("###   2 - NO                         ###")
        print("########################################")
    elif value == 12:
        print("########################################")
        print("Great!\nCan you beat your previous score?")
        print("########################################")
    elif value == 13:
        print("########################################")
        print("Thanks for playing.\nSee you next time!")
        print("########################################")
    elif value == 14:
        print("########################################")
        print("###            GAME OVER             ###")
        print("########################################")


# Method that gets the secret word from the opponent to set up the match
def secret():
    logos(2)
    global SECRET_WORD
    SECRET_WORD = input("Input a Secret Word: ")


# Method that shows the game modes to the player
def game_mode():
    logos(3)
    selection()


# Method that get the selected game mode from the player
def selection():
    option = int(input("Select a mode: "))
    global TRIES, GAME_MODE_VALUE
    if option == 1:
        TRIES = EASY_MODE
        GAME_MODE_VALUE = option
        logos(4)
    elif option == 2:
        GAME_MODE_VALUE = option
        TRIES = NORMAL_MODE
        logos(5)
    elif option == 3:
        GAME_MODE_VALUE = option
        TRIES = HARD_MODE
        logos(6)
    else:
        logos(7)
        selection()


# Method that get a guess word o char from the player and returns the value
def guess_word():
    user_guess = input("Input a Guess: ")
    print(user_guess)
    return user_guess


# Method that checks if the guess word is correct or not
def check(guess):
    global SCORE, TRIES
    if TRIES > 0:
        if guess == SECRET_WORD:
            SCORE += WINNING_BONUS
            score_calc()
            logos(8)
            replay()
        elif guess in SECRET_WORD:
            SCORE -= IS_IN_THE_GUESS
            TRIES -= len(guess)
            logos(9)
            play()
        else:
            TRIES -= 1
            SCORE -= IS_NOT_IN_THE_GUESS
            logos(10)
            play()
    else:
        logos(14)
        replay()
        return 0


# Method that calculates the score based on the game mode
def score_calc():
    global SCORE, TRIES, GAME_MODE_VALUE
    if GAME_MODE_VALUE == 1:
        SCORE += TRIES * 5
    elif GAME_MODE_VALUE == 2:
        SCORE += TRIES * 7
    elif GAME_MODE_VALUE == 3:
        SCORE += TRIES * 10


# Method that asks the user if he wants to play again or close the application
def replay():
    logos(11)
    option = int(input(""))
    if option == 1:
        logos(12)
        run()
    else:
        logos(13)
        return 0


run()
