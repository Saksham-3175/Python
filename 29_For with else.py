#For loop with else block
#The else block will execute only if the loop completes without any break statement. It means that loop is not break but exhausted.
#The else block can be uesd in while loop also.

for i in range(6):
    print(i)
else:
    print("Exhausted")

for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print("Exhausted")