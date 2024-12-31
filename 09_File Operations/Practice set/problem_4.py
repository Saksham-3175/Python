word = 'donkey'

def read_file():
    with open("donkey.txt") as read_file:
        global original_content #Making the variable content global.
        original_content = read_file.read()
        print(original_content)

def write_file():
    original_content
    global new_content 
    new_content = original_content.replace(word, '####')
    with open('donkey.txt', 'w') as write_file:
        write_file.write(new_content)
        print(new_content)

def revert_file():
    global new_content
    revert_content = new_content.replace('####', word)
    with open('donkey.txt', 'w') as write_file_1:
        write_file_1.write(revert_content)
        print(revert_content)

# read_file()
# write_file()
# revert_file()

def read_write_revert():
    read_file()
    write_file()
    revert_file()
read_write_revert()
