#Custom error are used to raise an exception with a message of our choice. We can raise errors with custom messages using the raise keyword and providing the type of error and the message.
#Its like 2 sides of a coin. One side is we are handling the error so that the program doesn't comes to a complete halt and the other side is before anything goes wrong further, we are raising an error to alert the user.
#To raise an error, we have to use the raise keyword and the type of error we want to raise. We can also optionally provide an error message with the error type.

a = input("Enter a number between 1 and 10: ")

def table(num):
    for i in range(1, 6):
        print(f"{num} X {i} = {num * i}")

try:
    if a.lower() == "quit":
        print("Quitting")
    else:
        num = int(a)
        if 1 <= num <= 10:
            table(num)
        else:
            raise ValueError("PLEASE ENTER A NUMBER BETWEEN 1 AND 10")
except ValueError as ve:
    print(ve)
except:
    raise ValueError("Invalid input. Please enter a number between 1 and 10 or 'quit' to exit.")
