def membershipchk(s):
    ch = input("Enter a charatcer to check : ")
    if ch in s:
        print("Present")
    else:
        print("Not present")

def length(s):
    count = 0
    for i in s:
        count+=1
    print(count,"Including all the spaces")

def strslice(s):
    i = int(input("Enter the index to slice to "))
    print("Sliced String :",s[:i])

def concat(s):
    n = input("Enter another string : ")
    s = s +" "
    print("After Concatination : ",s+n)
    
print("--------Welcome to Akanksh joshi String Manupilator--------")
print("Operations Available")
print("1. Membership check")
print("2. Length of the string")
print("3. slice the sting")
print("4. String Concatenation")
n = int(input("Choose an option : "))
m = input("Enter a String : ")
if n == 1 :
    membershipchk(m)
elif n == 2:
    length(m)
elif n == 3:
    strslice(m)
elif n == 4:
    concat(m)
else:
    print("Invalid Option")


