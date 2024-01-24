def cancel_appointment(dlist, mn, nm, dt, d):
   
    un =  int(input("Please provide the mobile number under which your booking has been made:"))
    if mn == un:
        op = input("Are you sure, would you like to cancel booking? yes/no: ")
        print()
        if op == "yes":
            print(f"Hello! {nm} your appointment has been cancelled with {dlist[d - 1]} on {dt}")
            input()
        else:
            print(f"Hello! {nm} your appointment is not cancelled.")
            input()
        
    else:
        print("No booking found with this number...Enter a valid number")