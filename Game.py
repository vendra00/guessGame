# Undefined Global Variables
SECRET_WORD: str
CORRECT_CHARS: str
INCORRECT_CHARS: str
GAME_MODE_VALUE: int
TRIES: int

# Defined Global Variables
IS_IN_THE_GUESS: int = 5
IS_NOT_IN_THE_GUESS: int = 10
WINNING_BONUS: int = 100
EASY_SCORE_MULTIPLIER: int = 10
NORMAL_SCORE_MULTIPLIER: int = 30
HARD_SCORE_MULTIPLIER: int = 70
EASY_MODE_TRIES: int = 10
NORMAL_MODE_TRIES: int = 7
HARD_MODE_TRIES: int = 4
CURRENT_SCORE: int = 0
HIGH_SCORE: int = 0


# Method that starts the match
def run():
    secret()
    game_mode()
    logos(1, None)
    play()


# Method that make a play in the game
def play():
    logos(15, None)
    check(guess_word())


# Method that contains all messages outputs from the application
def logos(value, element):
    if value == 1:
        print("========================================")
        print("===          TIME TO PLAY            ===")
        print("========================================")
    elif value == 2:
        print("========================================")
        print("===    WELCOME TO GUESS THE WORD     ===")
        print("========================================")
    elif value == 3:
        print("========================================")
        print("===       SELECT A GAME MODE         ===")
        print("========================================")
        print("===       1 - EASY                   ===")
        print("===       2 - NORMAL                 ===")
        print("===       3 - HARD                   ===")
        print("========================================")
    elif value == 4:
        print("========================================")
        print("You will have : " + str(TRIES) + " attempts.\nGood Luck!")
        print("========================================")
    elif value == 5:
        print("You will have : " + str(TRIES) + " attempts.\nGood Luck!")
    elif value == 6:
        print("You will have : " + str(TRIES) + " attempts.\nGood Luck!")
    elif value == 7:
        print("No game mode with the given option!")
    elif value == 8:
        print("========================================")
        print("===            You Win!              ===")
        print("===         Total Score: " + str(CURRENT_SCORE) + "         ===")
        print("========================================")
    elif value == 9:
        print("The word has this letters: ")
    elif value == 10:
        print("Keep Trying")
    elif value == 11:
        print("========================================")
        print("===   Do you want to play again?     ===")
        print("===   1 - YES                        ===")
        print("===   2 - NO                         ===")
        print("========================================")
    elif value == 12:
        print("Great!\nCan you beat your previous score?")
    elif value == 13:
        print("Thanks for playing.\nSee you next time!")
    elif value == 14:
        print("########################################")
        print("###            GAME OVER             ###")
        print("########################################")
    elif value == 15:
        print("You still have " + str(TRIES) + " attempts left")
    elif value == 16:
        print("The character '" + element + "'" + " is correct!")
    elif value == 17:
        print("The character '" + element + "'" + " is not correct!")
    elif value == 18:
        print("========================================")
        print("===        CONGRATULATIONS!          ===")
        print("===   YOU HIT A NEW HIGH SCORE!      ===")
        print("========================================")
        print("===   PREVIUS HIGH SCORE: " + str(HIGH_SCORE))
        print("===   NEW HIGH SCORE: " + str(CURRENT_SCORE))
        print("========================================")


# Method that gets the secret word from the opponent to set up the match
def secret():
    logos(2, None)
    global SECRET_WORD
    SECRET_WORD = input("Input a Secret Word: ").lower()


# Method that shows the game modes to the player
def game_mode():
    logos(3, None)
    selection()


# Method that get the selected game mode from the player
def selection():
    option = int(input("Select a mode: "))
    global TRIES, GAME_MODE_VALUE
    if option == 1:
        TRIES = EASY_MODE_TRIES
        GAME_MODE_VALUE = option
        logos(4, None)
    elif option == 2:
        GAME_MODE_VALUE = option
        TRIES = NORMAL_MODE_TRIES
        logos(5, None)
    elif option == 3:
        GAME_MODE_VALUE = option
        TRIES = HARD_MODE_TRIES
        logos(6, None)
    else:
        logos(7, None)
        selection()


# Method that get a guess word o char from the player and returns the value
def guess_word():
    user_guess = input("Input a Guess: ")
    print(user_guess)
    return user_guess


# Method that checks if the guess word is correct or not
def check(guess: str):
    global CURRENT_SCORE, TRIES
    if TRIES > 0:
        if guess == SECRET_WORD:
            CURRENT_SCORE += WINNING_BONUS
            score_calculator()
            logos(8, None)
            check_high_score()
            replay()
        elif guess in SECRET_WORD:
            CURRENT_SCORE -= IS_IN_THE_GUESS
            check_correct_caracters(guess)
            logos(9, None)
            play()
        else:
            check_correct_caracters(guess)
            CURRENT_SCORE -= IS_NOT_IN_THE_GUESS
            logos(10, None)
            play()
    else:
        logos(14, None)
        replay()
        return 0


# Method that checks if the given guess has some correct or incorrect characters
def check_correct_caracters(guess: str):
    global TRIES
    for element in guess:
        if element in SECRET_WORD:
            logos(16, element)
        else:
            logos(17, element)
            if TRIES > 0:
                TRIES -= 1
            else:
                logos(14, None)
                replay()



# Method that calculates the score based on the game mode
def score_calculator():
    global CURRENT_SCORE
    if GAME_MODE_VALUE == 1:
        CURRENT_SCORE += TRIES * EASY_SCORE_MULTIPLIER
    elif GAME_MODE_VALUE == 2:
        CURRENT_SCORE += TRIES * NORMAL_SCORE_MULTIPLIER
    elif GAME_MODE_VALUE == 3:
        CURRENT_SCORE += TRIES * HARD_SCORE_MULTIPLIER


# Method that checks if a new high score is set
def check_high_score():
    global HIGH_SCORE
    if CURRENT_SCORE > HIGH_SCORE:
        logos(18, None)
        HIGH_SCORE = CURRENT_SCORE


# Method that asks the user if he wants to play again or close the application
def replay():
    global CURRENT_SCORE
    logos(11, None)
    option = int(input(""))
    if option == 1:
        logos(12, None)
        CURRENT_SCORE = 0
        run()
    else:
        logos(13, None)
        return 0


run()
