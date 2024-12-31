with open('log.txt') as f:
    read = f.readlines()
line_no = 1
for line in read:
    if ('python' in line):
        print(f"The word is found at line: {line_no}")
        break
    line_no += 1
else:
    print("The word is not found")