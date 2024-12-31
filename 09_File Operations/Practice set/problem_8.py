content = ("Remove my content!!!")
with open('empty_this.txt', 'w') as f:
    empty_content = f.write(content)
with open('empty_this.txt') as f:
    content = f.read()
#At this point, empty_this.txt was created and now copying it into another one or renmaing it.
with open('new.txt','w') as f:
    f.write(content)

with open('empty_this.txt', 'w') as f:
    f.write("")