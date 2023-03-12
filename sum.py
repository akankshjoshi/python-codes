import csv
def write():
    f = open("details.csv","w")
    wo =csv.writer(f)
    wo.writerow(["UserId","Password"])
    while True:
        u_id=input("Enter User - Id : ")
        pswd=input("Enter Password : ")
        data=[u_id,pswd]
        wo.writerow(data)
        ch=input("Do you want to enter more record (you want to enter record(y/n)")
        if ch in 'Nn':
            break
        f.close()
        write()


