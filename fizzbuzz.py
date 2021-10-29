"""Play FizzBuzzWozz"""


def game_params():
    """
    User input for last and first numbers to play.
    """

    def game_end():
        """
        User input for last playable number.
        - checks number is integer
        - allows for negative numbers

        Returns:
            play_to : {int} -- Last playable number
        """

        game_end_str = "Please input the last number you wish to play:"
        game_end_input = input(game_end_str)
        while not game_end_input.isdigit():
            if "-" in game_end_input:
                if game_end_input.find("-") == 0:
                    game_end_input = game_end_input[1:len(game_end_input)]
                if game_end_input.isdigit():
                    play_to = int(game_end_input)
                    play_to = play_to * -1
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
        while not game_start_input.isdigit() \
                or play_to < int(game_start_input):
            if "-" in game_start_input:
                if game_start_input.find("-") == 0:
                    gsi = game_start_input
                    game_start_input = gsi[1:len(game_start_input)]
                if game_start_input.isdigit():
                    num = int(game_start_input)
                    num = num * -1
                    if play_to > num:
                        return num
            print(f"Please input a whole number lower than {play_to + 1}!")
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
        concat : {str} -- if divisble by multiple
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
        concat : {str} -- if divisble by multiple
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


def play(play_num, diff):
    """
    run the game
    """

    def compute_number(play_num):
        """
        checks if the number is divisible by 3, 5 and 4 or all, depending on\n
        difficulty settings and responds accordingly

        Parameters:
            num {int}  -- current playable number
        Returns:
            "f?b?z?" : {string} -- if divisible by difficulty number
            num : {num} -- if not divisible
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

    def check_number(play_num):
        minus = False
        player_guess = input("Please input your guess:")
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
        if "-" in player_guess:
            if player_guess.find("-") == 0:
                player_guess = player_guess[1:len(player_guess)]
                minus = True
        if player_guess.isdigit():
            player_guess = int(player_guess)
            if minus:
                player_guess = player_guess * -1
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
            # fizzbuzzwozz
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

    if play_num % 2 != 0:
        go_check = "computer"
    else:
        go_check = "player"

    if go_check == "player":
        check_number(play_num)
    else:
        print(compute_number(play_num))
    play_num += 1
    if play_num - 1 == play_end:
        return
    play(play_num, diff)


def check_diff():
    "check the difficulty"

    numbers = "Numbers divisible by "
    replace = " should be replaced by "
    three = f"{numbers}3{replace}'fizz'"
    five = f"{numbers}5{replace}'buzz'"
    four = f"{numbers}4{replace}'wozz'"
    three_five = f"{numbers}3 and 5{replace}'fizzbuzz'"
    three_four = f"{numbers}3 and 4{replace}'fizzwozz'"
    four_five = f"{numbers}4 and 5{replace}'wozzbuzz'"
    three_four_five = f"{numbers}3 and 4 and 5{replace}'fizzwozzbuzz'"

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

    # print rules
    if difficulty == "easy":
        print("You are playing on easy:")
        print(five)
    if difficulty == "medium":
        print("You are playing on medium:")
        print(three)
        print(five)
        print(three_five)
    if difficulty == "hard":
        print("You are playing on hard:")
        print(three)
        print(five)
        print(four)
        print(three_five)
        print(three_four)
        print(four_five)
        print(three_four_five)
    print("The case of your words does not matter, the order does!")
    if play_start % 2 == 0:
        print("You start!")
    else:
        print("Computer starts!")
    return difficulty


print("Hey there! Let's play FizzBuzz")
DIFF_STRING = "What difficulty would you like to play: easy, medium or hard:"
params = game_params()
play_end = params[0]
play_start = params[1]

play(play_start, check_diff())
print("Congratulations, you played the whole game!")
print("Thanks for playing!")
