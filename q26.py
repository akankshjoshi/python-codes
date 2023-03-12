file = open("myfile.txt","r")
counter = 0
content = file.read()
CoList = content.split("\n")
for i in CoList:
    if i:
        counter += 1
print("this is the number of lines in the file")
print(counter)        