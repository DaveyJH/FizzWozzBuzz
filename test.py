"""
A doctsring explaining what the file does
"""
import fizzbuzz

print("end of fizzbuzz!")

def example():
    """
    does some stuff
    """

    age = 16

    while age <= 18:
        if age <= 18:
            age += 1
            print(age)
        else:
            raise SystemExit('You must be older than 18!')

example()

print("Hello world! is a", type("Hello, World!"))
print(42, "is a", type(42))
print(3.145, "is a", type(3.145))
print(1j, "is a", type(1j))
print(["egg", "bacon", "spam"], "is a", type(["egg", "bacon", "spam"]))
print(("egg", "bacon", "spam"), "is a", type(("egg", "bacon", "spam")))
print(range(6), "is a", type(range(6)))
print({"name" : "John", "age" : 80}, "is a", type({"name" : "John", "age" : 80}))
print({"egg", "bacon", "spam"}, "is a", type({"egg", "bacon", "spam"}))
print(True, "is a", type(True))

print("when".center(26))
print("using the center".center(26))
print("method".center(26))
print("the result".center(26))
print("is".center(26))
print("this".center(26))
print(str("thisthatother".rpartition("that")))
