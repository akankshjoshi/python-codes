def prefix(name,gender):
 if gender == "M":
    name = "Mr."+name
    print(name)
 if gender == "F":
    name = "Ms."+name
    print(name)
name = input("Enter your name :")
gender = input("gender(ONLY TWO GENDERS M/F): ")
prefix(name,gender)