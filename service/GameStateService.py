import logging


def game_state(state: int):
    logging.info('Game State value (%s) - called', state)
    match state:
        case 1:
            print("========================================")
            print("===   WELCOME TO TREASURE HUNTERS    ===")
            print("========================================")
        case 2:
            print("========================================")
            print("===            GAME MENU             ===")
            print("========================================")
            print("===       1 - NEW GAME               ===")
            print("===       2 - LOAD GAME              ===")
            print("===       3 - OPTIONS                ===")
            print("===       4 - EXIT                   ===")
            print("========================================")
        case 3:
            print("========================================")
            print("===            NEW GAME              ===")
            print("========================================")
            print("===       CREATE A CHARACTER         ===")
            print("========================================")
        case 4:
            print("========================================")
            print("===         Character Name           ===")
            print("========================================")
        case 5:
            print("========================================")
            print("===         Character Gender         ===")
            print("========================================")
            print("===   1 - MALE                       ===")
            print("===   2 - FEMALE                     ===")
            print("========================================")
        case 6:
            print("========================================")
            print("===         Character Class          ===")
            print("========================================")
            print("===   1 - WIZARD                     ===")
            print("===   2 - WARRIOR                    ===")
            print("===   3 - ROGUE                      ===")
            print("========================================")
        case 7:
            print("========================================")
            print("===         Character Race           ===")
            print("========================================")
            print("===   1 - HUMAN                      ===")
            print("===   2 - ELF                        ===")
            print("===   3 - DWARF                      ===")
            print("===   4 - ORC                        ===")
            print("===   5 - GOBLIN                     ===")
            print("===   6 - GNOME                      ===")
            print("===   7 - HALF GIANT                 ===")
            print("========================================")
        case 100:
            print("========================================")
            print("===      Not a proper option!        ===")
            print("===                                  ===")
            print("===          Try it again            ===")
            print("========================================")
        case 101:
            print("========================================")
            print("===      Name cannot be empty        ===")
            print("===       or a numeric value         ===")
            print("===                                  ===")
            print("===          Try it again            ===")
            print("========================================")
