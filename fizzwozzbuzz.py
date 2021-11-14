"""
CLI playable version of FizzBuzz with multiple
difficulties and input validation
"""


def convert_to_negative(user_input):
    """
    Converts user input to negative integer if preceded by '-'

    Paramaters:
        input : {str} -- user input received

    Returns:
        playNumber : {int} -- negative integer for game play
    """

    if user_input.find("-") == 0:
        user_input = user_input[1:len(user_input)]
    if user_input.isdigit():
        play_number = int(user_input)
        play_number = play_number * -1
        return play_number

    return user_input


def game_end():
    """
    User input for last playable number.
    - checks number is integer
    - allows for negative numbers

    Returns:
        play_to : {int} -- last playable number
    """

    game_end_str = "Please input the last number you wish to play:"
    game_end_input = input(game_end_str)
    while not game_end_input.isdigit():
        if "-" in game_end_input:
            play_to = convert_to_negative(game_end_input)
            return play_to
        print("Please pick a whole number!")
        game_end_input = input(game_end_str)
        continue
    if game_end_input.isdigit():
        play_to = int(game_end_input)
        return play_to
    else:
        raise SystemExit("Something went wrong with game_end()")


def game_start(play_to):
    """
    User input for first number in game.
    - checks number is integer
    - checks number is lower than last playable number
    - allows for negative numbers

    Parameters:
        play_to : {int}  -- last playable number
    Returns:
        num : {int} -- first number in game
    """

    game_start_input = input("Please input a starting number:")
    while (
        not game_start_input.isdigit()
        or play_to <= int(game_start_input)
    ):
        if "-" in game_start_input:
            num = convert_to_negative(game_start_input)
            if play_to > num:
                return num
        print(f"Please input a whole number lower than {play_to}!")
        game_start_input = input("Please input a starting number:")
        continue
    if game_start_input.isdigit():
        num = int(game_start_input)
        return num
    else:
        raise SystemExit("Something went wrong with game_start()")

    end = game_end()
    return (end, game_start(end))


def play_easy(play_num):
    """
    checks if number if divisible by 5
    returns:
        buzz : {str} -- if divisible by 5
        play_num : {int} -- if not divisible by 5
    """

    if play_num % 5 == 0:
        result = "buzz"
    else:
        result = play_num
    return result


def play_med(play_num):
    """
    checks if number is divisible by 3 or 5
    returns:
        buzz : {str} -- if divisible by 5
        fizz : {str} -- if divisible by 3
        concat : {str} -- if divisible by multiple
        play_num : {int} -- if not divisible by 3 or 5
    """

    if play_num % 5 == 0 and play_num % 3 == 0:
        result = "fizzbuzz"
    elif play_num % 3 == 0:
        result = "fizz"
    elif play_num % 5 == 0:
        result = "buzz"
    else:
        result = play_num
    return result


def play_hard(play_num):
    """
    checks if number is divisible by 3 or 5 or 4
    returns:
        buzz : {str} -- if divisible by 5
        fizz : {str} -- if divisible by 3
        wozz : {str} -- if divisible by 4
        concat : {str} -- if divisible by multiple
        play_num : {int} -- if not divisible by 3 or 5
    """

    if play_num % 5 == 0 and play_num % 3 == 0 and play_num % 4 == 0:
        result = "fizzwozzbuzz"
    elif play_num % 5 == 0 and play_num % 3 == 0:
        result = "fizzbuzz"
    elif play_num % 4 == 0 and play_num % 3 == 0:
        result = "fizzwozz"
    elif play_num % 5 == 0 and play_num % 4 == 0:
        result = "buzzwozz"
    elif play_num % 3 == 0:
        result = "fizz"
    elif play_num % 5 == 0:
        result = "buzz"
    elif play_num % 4 == 0:
        result = "wozz"
    else:
        result = play_num
    return result


def check_diff():
    """check the difficulty"""

    NUMBERS = "Numbers divisible by "
    REPLACE = " should be replaced by "
    THREE = f"{NUMBERS}3{REPLACE}'fizz'"
    FIVE = f"{NUMBERS}5{REPLACE}'buzz'"
    FOUR = f"{NUMBERS}4{REPLACE}'wozz'"
    THREE_FIVE = f"{NUMBERS}3 and 5{REPLACE}'fizzbuzz'"
    THREE_FOUR = f"{NUMBERS}3 and 4{REPLACE}'fizzwozz'"
    FOUR_FIVE = f"{NUMBERS}4 and 5{REPLACE}'wozzbuzz'"
    THREE_FOUR_FIVE = f"{NUMBERS}3 and 4 and 5{REPLACE}'fizzwozzbuzz'"
    DIFF_STRING = "What difficulty would you like to play: "\
        "easy, medium or hard:"

    difficulty = input(DIFF_STRING).lower()
    while not difficulty.isalpha():
        print("Please input 'easy', 'medium' or 'hard'")
        difficulty = input(DIFF_STRING).lower()
        continue

    while difficulty not in ("easy", "medium", "hard"):
        while difficulty[0] == "e":
            mean_easy = input("Did you mean 'easy'? y/n:")
            if mean_easy == "n":
                break
            elif mean_easy == "y":
                difficulty = "easy"
                break
            else:
                print("Invalid response")
                continue
        while difficulty[0] == "m":
            mean_med = input("Did you mean 'medium'? y/n:")
            if mean_med == "n":
                break
            elif mean_med == "y":
                difficulty = "medium"
                break
            else:
                print("Invalid response")
                continue
        while difficulty[0] == "h":
            mean_hard = input("Did you mean 'hard'? y/n:")
            if mean_hard == "n":
                break
            elif mean_hard == "y":
                difficulty = "hard"
                break
            else:
                print("Invalid response")
                continue
        if difficulty not in ("easy", "medium", "hard"):
            print("Please input 'easy', 'medium' or 'hard'")
            difficulty = input(DIFF_STRING).lower()
            continue

    if difficulty == "easy":
        print("You are playing on easy:")
        print(FIVE)
    if difficulty == "medium":
        print("You are playing on medium:")
        print(THREE)
        print(FIVE)
        print(THREE_FIVE)
    if difficulty == "hard":
        print("You are playing on hard:")
        print(THREE)
        print(FIVE)
        print(FOUR)
        print(THREE_FIVE)
        print(THREE_FOUR)
        print(FOUR_FIVE)
        print(THREE_FOUR_FIVE)
    print("The case of your words does not matter, the order does!")
    if play_start % 2 == 0:
        print("You start!")
    else:
        print("Computer starts!")
    return difficulty


def compute_number(play_num, diff):
    """
    Checks if the number is divisible by 3, 5 and 4 or all, depending on
    difficulty settings and responds accordingly

    Parameters:
        play_num {int}  -- current playable number
        diff {str} : -- difficulty level
    Returns:
        "f?w?b?" : {string} -- if divisible by difficulty number
        num : {int} -- if not divisible
    """

    if diff == "easy":
        result = play_easy(play_num)
    elif diff == "medium":
        result = play_med(play_num)
    elif diff == "hard":
        result = play_hard(play_num)
    else:
        raise SystemExit(
            "Something went wrong with the difficulty settings!")
    return result


def check_number(play_num, diff):
    """
    Check user input

    Parameters:
        play_num : {int} -- number to be played
        diff : {str} -- difficulty level
    """

    minus = False
    player_guess = input("Please input your guess:")

    # check for spaces
    if "".join(player_guess.split()).isalpha():
        player_guess = player_guess.lower()
        valid_words = [
            "fizz",
            "buzz",
            "wozz",
            "fizzbuzz",
            "fizzwozz",
            "wozzbuzz"
        ]
        guess_list = player_guess.split()
        if all(word in valid_words for word in guess_list):
            player_guess = "".join(player_guess.split())

    # check for negative
    if "-" in player_guess:
        if player_guess.find("-") == 0:
            player_guess = player_guess[1:len(player_guess)]
            minus = True

    # convert to integer
    if player_guess.isdigit():
        player_guess = int(player_guess)
        if minus:
            player_guess = player_guess * -1

    # check for correct response
    if diff == "easy":
        # buzz
        if play_num % 5 == 0:
            if player_guess == "buzz":
                pass
            else:
                print("I'm sorry, you lost.")
                print("That should have been 'buzz'.")
                print("Better luck next time!! Now BUZZ off!!")
                exit()
        # number
        else:
            if player_guess == play_num:
                pass
            else:
                print(f"Sorry, that should have been {play_num}!")
                print("You lose, your number is up!!")
                exit()

    if diff == "medium":
        # number
        if play_num % 5 != 0 and play_num % 3 != 0:
            if player_guess == play_num:
                pass
            else:
                print(f"Sorry, that should have been {play_num}!")
                print("You lose, your number is up!!")
                exit()
        # fizzbuzz
        if play_num % 5 == 0 and play_num % 3 == 0:
            if player_guess == "fizzbuzz":
                pass
            else:
                print("I'm sorry, you lost.")
                print("That should have been 'fizzbuzz'.")
                print("Better luck next time!!")
                print("You really FIZZled out!!")
                print("Now BUZZ off!!")
                exit()
        # buzz
        if play_num % 5 == 0 and play_num % 3 != 0:
            if player_guess == "buzz":
                pass
            else:
                print("I'm sorry, you lost.")
                print("That should have been 'buzz'.")
                print("Better luck next time!! Now BUZZ off!!")
                exit()
        # fizz
        if play_num % 5 != 0 and play_num % 3 == 0:
            if player_guess == "fizz":
                pass
            else:
                print("I'm sorry, you lost.")
                print("That should have been 'fizz'.")
                print("Better luck next time!! You really FIZZled out!!")
                exit()

    if diff == "hard":
        # number
        if (play_num % 5 != 0
            and play_num % 3 != 0
                and play_num % 4 != 0):
            if player_guess == play_num:
                pass
            else:
                print(f"Sorry, that should have been {play_num}!")
                print("You lose, your number is up!!")
                exit()
        # fizzwozzbuzz
        if (play_num % 5 == 0
            and play_num % 3 == 0
                and play_num % 4 == 0):
            if player_guess == "fizzwozzbuzz":
                pass
            else:
                print("I'm sorry, you lost.")
                print("That should have been 'fizzwozzbuzz'.")
                print("Better luck next time!!")
                print("You really FIZZled out!!")
                print("That WOZZ fun!!")
                print("Now BUZZ off!!")
                exit()
        # fizzbuzz
        if (play_num % 5 == 0
            and play_num % 3 == 0
                and play_num % 4 != 0):
            if player_guess == "fizzbuzz":
                pass
            else:
                print("I'm sorry, you lost.")
                print("That should have been 'fizzbuzz'.")
                print("Better luck next time!!")
                print("You really FIZZled out!!")
                print("Now BUZZ off!!")
                exit()
        # wozzbuzz
        if (play_num % 5 == 0
            and play_num % 3 != 0
                and play_num % 4 == 0):
            if player_guess == "wozzbuzz":
                pass
            else:
                print("I'm sorry, you lost.")
                print("That should have been 'wozzbuzz'")
                print("Better luck next time!!")
                print("That WOZZ fun!!")
                print("Now BUZZ off!!")
                exit()
        # fizzwozz
        if (play_num % 5 != 0
            and play_num % 3 == 0
                and play_num % 4 == 0):
            if player_guess == "fizzwozz":
                pass
            else:
                print("I'm sorry, you lost.")
                print("That should have been 'fizzwozz'.")
                print("Better luck next time!!")
                print("You really FIZZled out!!")
                print("That WOZZ fun!!")
                exit()
        # buzz
        if (play_num % 5 == 0
            and play_num % 3 != 0
                and play_num % 4 != 0):
            if player_guess == "buzz":
                pass
            else:
                print("I'm sorry, you lost.")
                print("That should have been 'buzz'.")
                print("Better luck next time!! Now BUZZ off!!")
                exit()
        # fizz
        if (play_num % 5 != 0
            and play_num % 3 == 0
                and play_num % 4 != 0):
            if player_guess == "fizz":
                pass
            else:
                print("I'm sorry, you lost.")
                print("That should have been 'fizz'.")
                print("Better luck next time!! You really FIZZled out!!")
                exit()
        # wozz
        if (play_num % 5 != 0
            and play_num % 3 != 0
                and play_num % 4 == 0):
            if player_guess == "wozz":
                pass
            else:
                print("I'm sorry, you lost.")
                print("That should have been 'wozz'.")
                print("Better luck next time!! That WOZZ fun!!")
                exit()


def play(play_num, diff):
    """
    Run the game

    Parametes:
        play_num : {int} -- first number to be played
        diff : {str} -- difficulty level
    """

    if play_num % 2 != 0:
        print(compute_number(play_num, diff))
    else:
        check_number(play_num, diff)

    play_num += 1
    if play_num - 1 == play_end:
        return
    play(play_num, diff)


print("Hey there! Let's play FizzBuzz")
play_end = game_end()
play_start = game_start(play_end)

play(play_start, check_diff())
print("Congratulations, you played the whole game!")
print("Thanks for playing!")
exit()