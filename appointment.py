def appointment(dlist):

    print("\t\t\tENTER YOUR DETAILS")
    nm = input("Name: ")
    mn = int(input("Mob No: "))
    dt = input("Date: ")
    print("Doctors available:")
    print()
    for i,j in enumerate (dlist):
        print(i+1,".",j)
    print()
    d = int(input("Enter doctor's id: "))
    print(f"Hello! {nm} your appointment has been booked with {dlist[d - 1]} on {dt}.")

    return dt, mn, nm, d