def find_a_doctor(db):
    print("\t\t\tAVAILABLE DOCTORS")

    col = db["doctors"]
    for j,i in enumerate (col.find()):
        print(str(j+1) + '.',i['doctor_name'],i['specification'])

    # print("""
    # 1. Dr. Karthik, MD (Medical Doctor)
    # 2. Dr. Prince Sanjivy, DO (Doctor of Osteopathic Medicine)
    # 3. Dr. Vasanth, DDS (Doctor of Dental Surgery)
    # 4. Dr. Vijay, DVM (Doctor of Veterinary Medicine)
    # 5. Dr. Gowtham, PsyD (Doctor of Psychology)
    # 6. Dr. Raj Kumar, MD (Medical Doctor) 
    # """)
    