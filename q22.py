writemode = open("Q22data.txt","w")
writemode.write("abcdefghijklmnopqrstuvwxyz")
writemode.close()

readmode = open("Q22data.txt","r")
print(readmode.tell())
readmode.seek(4)
print(readmode.read(5))
readmode.seek(14)   
print(readmode.tell())
print(readmode.read(10))

readmode.close()