#file reading
# file = open("this.txt")
# data = file.read()
# print(data)
# file.close()

#file writing
# str = "This is a string file"
# file = open("string.txt", "w")
# file.write(str)
# file.close()

#Printing mulitiple lines from a file.
# keyboard = open("multiple.txt")
# data = keyboard.readline()
#for loop
# for line in data:
#     print(line)
# print(data, type(data))
#while loop
# while (data != ""):
#     print(data)
#     data = keyboard.readline()
# keyboard.close()

with open('new_file.txt', 'w') as f:
    f.write('This is a new file dated 1 Jan 2025')

# import PyPDF2
# with open('Personal Review.pdf', 'rb') as f:
#     reader = PyPDF2.PdfFileReader(f)
#     content = ""
#     for page_num in range(reader.numPages):
#         page = reader.getPage(page_num)
#         content += page.extract_text()
    
#     lines = content.split('\n')
#     for line in lines[:5]:
#         print(line)
    