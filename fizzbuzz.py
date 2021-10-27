playTo = int(input("Please state the last number you wish to play:"))
num = int(input("Please input a number:"))

def play(num):

    def checkNumber(num):

        """
        checks if the number is divisible by 3, 
        5 or both and responds accordinlgly
        @param {int} num
        """

        if num % 5 == 0 and num % 3 == 0:
            return "fizzbuzz"
        elif num % 3 == 0:
            return "fizz"
        elif num % 5 == 0:
            return "buzz"
        else:
            return num

        return

    print(checkNumber(num))
    num += 1
    if num - 1 == playTo:
        return
    play(num)
play(num)
SystemExit("Thanks for playing!")
