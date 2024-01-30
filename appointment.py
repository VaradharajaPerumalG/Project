def appointment(db):

    col = db["appointment"]
    print("\t\t\tENTER YOUR DETAILS")
    nm = input("Name: ")
    mn = int(input("Mob No: "))
    dt = input("Date: ")
    print("Doctors available:")
    print()
    col = db["doctors"]
    dlist = list(col.find())
    for j,i in enumerate (dlist):
        print(str(j+1) + '.',i['doctor_name'],i['specification'])
    print()
    d = int(input("Enter doctor's id: "))

    col = db["appointment"]
    total = len(list(col.find()))
    col.insert_one({"_id": total+1, "name": total+1, "mob_no": total+1, "doctor_id": total+1,  "date": total+1}
                )

    print(f"Hello! {nm} your appointment has been booked with {dlist[d - 1]["doctor_name"]} {dlist[d - 1]["specification"]} on {dt}.")

    return  dt, mn, nm, d 