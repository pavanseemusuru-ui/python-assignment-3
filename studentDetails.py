students={
    500:{
        "Name":"Manoj",
        "Age":20,
        "Marks":(98,95,87),
        "Sections":"CSE",
    },
    501:{
        "Name":"Gani",
        "Age":20,
        "Marks":(100,80,95),
        "Section":"CSE",
    },
    502:{
        "Name":"Hari", 
        "Age":19,
        "Marks":(99,88,79),
        "Section":"CSE",
    },
    503:{
        "Name":"Pavan",
        "Age":18,
        "Marks":(87,90,79),
        "Section":"CSE",
    },
    504:{
        "Name":"Ram",
        "Age":17,
        "Marks":(100,50,60),
        "Section":"CSE",
    }
}
roll = set(students)
print("REGISTERED roll numbers",roll)
user=0
while user !=6:
    user=int(input("Enter 1 for REGiSTERING new student :\nEnter 2 for DISPLAY all student details :\nEnter 3 for REMOVE student :\n" \
"Enter 4 to kno TOPPER of class : \nEnter 5 to SEARCH Student:\nEnter 6 TO EXIT() : "))
    if user == 1:
    
     while True:
        try:
            rol = int(input("Enter your roll number: "))
            break
        except ValueError:
            print("Invalid input! Please enter numbers only.")

     if rol in students:
          print("Roll number already exists. ")

     else:
         students[rol]={
             "Name":input("Enter your name : "),
             "Age":int(input("Enter your Age : ")),
             "Section":input("Enter your section : "),
             "Marks":(int(input("marks of S1 : ")),int(input("marks of S2 :")),int(input("marks of S3 :")))
         }
         print(students[rol]["Name"]," your registration completed.")
    elif user==2:
        print(students.items())
    elif user==3:
        rl=int(input("Enter roll number to REMOVE : "))
        if rl in students:
          print(students[rl]," removed....")
          students.pop(rl)
        else:
            print("No student have this roll number")
    elif user==4:
        high=0
        for m in students:
            marks=students[m]["Marks"]
            total=sum(marks)
            
            if total>high:
                high=total
                Topper=students[m]["Name"]
        print(Topper,"is the topper of class \nmarks :",high)
    elif user==5:
        while True:
         try:
            search = int(input("SEARCH enter roll number: "))
            break
         except ValueError:
            print("Invalid input! Please enter numbers only.")
        if search in students:
          print(students[search])
        else:
          print(search,": 5roll number is doesnot exist")
 