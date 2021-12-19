from model import Player

# Undefined Global Variables
SECRET_WORD: str
SECRET_WORD_BUILDER: str
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
    set_secret_word()
    game_mode()
    game_states(1)
    play()


def create_player():
    name: str = input("Player Name: ")
    player = Player.Player()
    player.set_name(name)
    print(player.get_name())


# Method that make a play in the game
def play():
    game_states(15)
    if TRIES > 0:
        check(guess_word())
    else:
        game_states(14)
        replay()


# Method that contains all messages outputs from the application
def game_states(value: int, element=None):
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
    elif value == 4 or value == 5 or value == 6:
        print("========================================")
        print("You will have : " + str(TRIES) + " attempts.\nGood Luck!")
        print("========================================")
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
        print("========================================")
        print("===              Great!              ===")
        print("========================================")
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
        print("===   PREVIOUS HIGH SCORE: " + str(HIGH_SCORE))
        print("===   NEW HIGH SCORE: " + str(CURRENT_SCORE))
        print("========================================")
    elif value == 19:
        print("========================================")
        print("===      Not a proper option!        ===")
        print("===          Try it again            ===")
        print("========================================")
    elif value == 20:
        print("Not a valid option!")


# Method that gets the secret word from the opponent to set up the match
def set_secret_word():
    game_states(2)
    global SECRET_WORD
    SECRET_WORD = input("Input a Secret Word: ").lower()


# Method that shows the game modes to the player
def game_mode():
    game_states(3)
    game_mode_set_up()


# Method that get the selected game mode from the player
def game_mode_set_up():
    global TRIES, GAME_MODE_VALUE
    option: int = 0
    try:
        option = int(input("Select a game mode: "))
    except ValueError:
        game_states(19)
        game_mode()
    if option == 1:
        TRIES = EASY_MODE_TRIES
        GAME_MODE_VALUE = option
        game_states(4)
    elif option == 2:
        GAME_MODE_VALUE = option
        TRIES = NORMAL_MODE_TRIES
        game_states(5)
    elif option == 3:
        GAME_MODE_VALUE = option
        TRIES = HARD_MODE_TRIES
        game_states(6)
    else:
        game_states(7)
        game_mode()


# Method that get a guess word to char from the player and returns the value
def guess_word():
    user_guess = input("Input a Guess: ")
    print(user_guess)
    return user_guess


# Method that checks if the guess word is correct or not
def check(guess: str):
    global CURRENT_SCORE, TRIES
    if guess == SECRET_WORD:
        CURRENT_SCORE += WINNING_BONUS
        score_calculator()
        game_states(8)
        check_high_score()
        replay()
    elif guess in SECRET_WORD:
        CURRENT_SCORE -= IS_IN_THE_GUESS
        check_correct_characters(guess)
        game_states(9)
        play()
    else:
        check_correct_characters(guess)
        CURRENT_SCORE -= IS_NOT_IN_THE_GUESS
        game_states(10)
        play()


# Method that checks if the given guess has some correct or incorrect characters
def check_correct_characters(guess: str):
    global TRIES
    for element in guess:
        if element in SECRET_WORD:
            game_states(16, element)
        else:
            game_states(17, element)
            if TRIES > 0:
                TRIES -= 1
            else:
                game_states(14)
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
        game_states(18)
        HIGH_SCORE = CURRENT_SCORE


# Method that asks the user if he wants to play again or close the application
def replay():
    global CURRENT_SCORE
    game_states(11)
    option: int = 0
    try:
        option = int(input(""))
    except ValueError:
        game_states(19)
        replay()
    if option == 1:
        game_states(12)
        CURRENT_SCORE = 0
        run()
    elif option == 2:
        game_states(13)
        return 0
    else:
        game_states(20)
        replay()


run()
