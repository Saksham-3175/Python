words = ['hacker', 'covid-19', 'terrorist', 'stabbed']
placeholders = {}
def read_file():
    global read_content
    with open('story.txt') as f:
        read_content = f.read()
    print(read_content)

def write_file():
    global write_content
    write_content = read_content
    for word in words:
        placeholder = f"{{{word}}}"
        write_content = write_content.replace(word, placeholder)
        placeholders[placeholder] = word
    with open('story.txt', 'w') as j:
        j.write(write_content)
    print(write_content)
def revert_file():
    global write_content #It is globalized again so ensure we are using the same variable.
    revert_content = write_content
    for placeholder, original_word in placeholders.items():
        revert_content = revert_content.replace(placeholder, original_word)
    with open('story.txt', 'w') as w:
        w.write(revert_content)
    print(revert_content)
def read_write_revert():
    read_file()
    write_file()
    revert_file()
read_write_revert()
        
# with open('story.txt') as f:
#     content = f.read()
#     print(content)

# for word in words:
#     #instead of creating a new variable, I updated the initial variable(content)
#     content = content.replace(word, ('*' * len(word)))

# with open('story.txt', 'w') as j:
#     j.write(content)
#     print(content)