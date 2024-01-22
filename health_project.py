import os
print("""
          #######     ###       ##       #### ######## ########     ######     ###    ########  ######## 
         ##     ##   ## ##      ##        ##  ##       ##          ##    ##   ## ##   ##     ## ##       
         ##     ##  ##   ##     ##        ##  ##       ##          ##        ##   ##  ##     ## ##       
         ##     ## ##     ##    ##        ##  ######   ######      ##       ##     ## ########  ######   
         ##     ## #########    ##        ##  ##       ##          ##       ######### ##   ##   ##       
         ##     ## ##     ##    ##        ##  ##       ##          ##    ## ##     ## ##    ##  ##       
          #######  ##     ##    ######## #### ##       ########     ######  ##     ## ##     ## ######## """)
print()
print()
print()
print()
print(input("PRESS ANY KEY TO CONTINUE..."))
os.system("cls")
print("""      
                                                
                                
                        ┌─────      •✧✧•     ─────┐                      
                          WELCOME TO OA LIFE CARE                
                        └─────      •✧✧•     ─────┘
      
                                      _   
                                    _| |_ 
                                   |_   _|
                                     |_|   
                                                                    
                            
       """)
print()
print(input("PRESS ANY KEY TO VIEW INFORMATIONS..."))
dlist = [
      "Dr. Karthik, MD (Medical Doctor)",
      "Dr. Prince Sanjivy, DO (Doctor of Osteopathic Medicine)",
      "Dr. Vasanth, DDS (Doctor of Dental Surgery)",
      "Dr. Vijay, DVM (Doctor of Veterinary Medicine)",
      "Dr. Gowtham, PsyD (Doctor of Psychology)",
      "Dr. Raj Kumar, MD (Medical Doctor)"
      ]
while True:
  print("MENU")
  print("""
  1. Find a Doctor
  2. Book Appointment
  3. Cancel Appointment
  4. About us
  5. Exit
  """)
  a = int(input("Choose an option:"))
  if a == 1:
      print("\t\t\tAVAILABLE DOCTORS")
      print("""
      1. Dr. Karthik, MD (Medical Doctor)
      2. Dr. Prince Sanjivy, DO (Doctor of Osteopathic Medicine)
      3. Dr. Vasanth, DDS (Doctor of Dental Surgery)
      4. Dr. Vijay, DVM (Doctor of Veterinary Medicine)
      5. Dr. Gowtham, PsyD (Doctor of Psychology)
      6. Dr. Raj Kumar, MD (Medical Doctor) 
      """)
  if a == 2:
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
  if a == 5:
     break  





   

       
       
