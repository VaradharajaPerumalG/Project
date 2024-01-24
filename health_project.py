import os
from pymongo.mongo_client import MongoClient
from find_a_doctor import find_a_doctor
from appointment import appointment
from cancel_appointment import cancel_appointment
from about_project import about_project

db_uri = "mongodb+srv://VaradharajaPerumal:54410@varadharajaperumal.jlcs4d1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(db_uri)


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
      
      find_a_doctor()
      input()
      os.system("cls")

  if a == 2:
      
      dt, mn, nm, d = appointment(dlist)
      input()
      os.system("cls")

  if a == 3:
       
       cancel_appointment(dlist,mn,nm,dt,d)
       input()
       os.system("cls")

  if a == 4:
     
     about_project()
     input()
     os.system("cls")    
     
  if a == 5:
     break  





   

       
       
