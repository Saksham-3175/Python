with open('story.txt') as f:
    content1 = f.read()

with open('donkey.txt') as f:
    content2 = f.read()

if (content1 == content2):
    print("Identical")
else:
    print("Not identical")