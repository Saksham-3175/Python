with open("problem_1.txt") as file:
    content = file.read()
    if ("machine" in content):
        print("The word 'machine' exists in the file")
    else:
        print("The word 'mahcine' does not exists in the file.")
print("Problem 1 sucessfully solved and closed.")




# file = open('problem_1.txt')
# content = file.read()
# if ("machine" in content):
#     print("The word 'machine' exists in the file")
# else:
#     print("The word 'machine' does not exists in the file.")
# file.close()