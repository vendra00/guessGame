secret_word: str
tries: int
score: int = 0
game_mode_value: int


def play():
    check(guess_word())


def run():
    secret()
    game_mode()
    logos(1)
    play()


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
        print("You will have : " + str(tries) + " attempts.\nGood Luck!")
        print("########################################")
    elif value == 5:
        print("########################################")
        print("You will have : " + str(tries) + " attempts.\nGood Luck!")
        print("########################################")
    elif value == 6:
        print("########################################")
        print("You will have : " + str(tries) + " attempts.\nGood Luck!")
        print("########################################")
    elif value == 7:
        print("########################################")
        print("No game mode with the given option!")
        print("########################################")
    elif value == 8:
        print("########################################")
        print("You Win!\nTotal Score: " + str(score))
        print("########################################")
    elif value == 9:
        print("########################################")
        print("The word has this letters: ")
        print("########################################")
    elif value == 10:
        print("########################################")
        print("Keep Trying")
        print("########################################")


def secret():
    logos(2)
    global secret_word
    secret_word = input("Input a Secret Word: ")


def game_mode():
    logos(3)
    selection()


def selection():
    option = int(input("Select a mode: "))
    global tries, game_mode_value
    if option == 1:
        tries = 10
        game_mode_value = option
        logos(4)
    elif option == 2:
        game_mode_value = option
        tries = 7
        logos(5)
    elif option == 3:
        game_mode_value = option
        tries = 4
        logos(6)
    else:
        logos(7)
        selection()


def guess_word():
    user_guess = input("Input a Guess: ")
    print(user_guess)
    return user_guess


def check(guess):
    global score, tries
    if guess == secret_word:
        score += 100
        score_calc()
        logos(8)
    elif guess in secret_word:
        score -= 5
        tries -= 1
        logos(9)
        play()
    else:
        tries -= 1
        score -= 10
        logos(10)
        play()


def score_calc():
    global score, tries, game_mode_value
    if game_mode_value == 1:
        score += tries * 5
    elif game_mode_value == 2:
        score += tries * 7
    elif game_mode_value == 3:
        score += tries * 10


run()
