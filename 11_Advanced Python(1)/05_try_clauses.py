#Try with else clause and finally clause

#Else: When you want to run a piece of code if 'Try' block runs sucessfully.

#Finally: Should be mainly used in functions. It runs regardless of what's happening in try or except block. But when you 'return' in either of the blocks(try & except), the code under finally would still run.

#without finally
def without_finally():
    try: 
        a = int(input("Enter a number: "))
        print(a)
        return ("Try return")
    except Exception as e:
        print(e)
        return ("Except return")
    print("I am inside finally block so I run no matter what")
# without_finally()
#The finally code won't be executed since after 'return' no code runs inside the function.

#with finally
def with_finally():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return print("Try Return")
    except Exception as e:
        print(e)
        return print("Except Return")
    finally:
        print("I run! It's what I do!!!")
with_finally()