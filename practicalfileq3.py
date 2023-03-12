print("enter the first string: ",end="")
string1 = input()
print("enter the second string: ",end="")
string2 = input()

print("\nString before swap:")
print("string1 =",string1)
print("string2 =",string2)

temp = string1
string1 = string2
string2 = temp

print("\nString after swap:")
print("string1 =",string1)
print("string2 =",string2)
