secret_word: str
tries: int


def play():
    check(guess())


def run():
    secret()
    game_mode()
    print("########################################")
    print("###          TIME TO PLAY            ###")
    print("########################################")
    play()


def secret():
    print("########################################")
    print("###    WELCOME TO GUESS THE WORD     ###")
    print("########################################")
    global secret_word
    secret_word = input("Input a Secret Word: ")


def game_mode():
    print("########################################")
    print("###       SELECT A GAME MODE         ###")
    print("########################################")
    print("###       1 - EASY                   ###")
    print("###       2 - NORMAL                 ###")
    print("###       3 - HARD                   ###")
    print("########################################")
    selection()


def selection():
    option = int(input("Select a mode: "))
    global tries
    if option == 1:
        tries = 10
        print("You will have : " + str(tries) + "attempts!")
    elif option == 2:
        tries = 7
        print("You will have : " + str(tries) + "attempts!")
    elif option == 3:
        tries = 4
        print("You will have : " + str(tries) + "attempts!")
    else:
        print("There is no game mode with the given option!")
        selection()


def guess():
    user_guess = input("Input a Guess: ")
    print(user_guess)
    return user_guess


def check(value):
    if value == secret_word:
        print("You Win!")
    elif value in secret_word:
        print("The word has this letters: ")
        play()
    else:
        print("Keep Trying")
        play()


run()
