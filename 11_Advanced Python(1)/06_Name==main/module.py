def greet():
    print("Hello User!!!")

print(__name__)


def explain():
    print('The code under the name == main will run if and only if it is executed from the module file...')
explain()
#The output will be __main__ as we are executing the code from this file itself.

if __name__ == "__main__":
    print('This is the code only for module file')
    greet()
