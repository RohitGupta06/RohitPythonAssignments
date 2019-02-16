# Designing The Marksheet

# Entering The Details
Full_Name = input("Plz enter Full Name of Student: ")
Father_Name = input("Plz enter Full Name of Father: ")
Roll_No = int(input("Plz enter student's Roll Number: "))
Course_Name = input("Plz enter course name: ")

# Entering The marks of all subjects
print("\nEnter the marks of all 5 subjects.")
Subj1 = int(input("Marks in Mathematics-III - "))
Subj2 = int(input("Marks in Analysis Design of Algorithms - "))
Subj3 = int(input("Marks in Software Engineering - "))
Subj4 = int(input("Marks in Computer Org. & Architecture - "))
Subj5 = int(input("Marks in Operating Systems - "))

# Calculating Total Marks and Percentage
Total_Marks = Subj1 + Subj2 + Subj3 + Subj4 + Subj5
Percentage = (Total_Marks/450) * 100

# Displaying the Marksheet
print('''
______________________________________________________________________________      
|{:^77}|
|                                                                             |
|Student's Name - {}                                                 |
|Father's Name - {}                                           |
|Student's Roll No. - {}                                                     |      
|Course Name - {}                                                        |      
|_____________________________________________________________________________|
|{:^5}|{:^12}|{:^41}|{:^16}|
|_____|____________|_________________________________________|________________|
|     |            |                                         |                |
|{:^5}|{:^12}|{:^41}|{:^16}|
|_____|____________|_________________________________________|________________|
|     |            |                                         |                |
|{:^5}|{:^12}|{:^41}|{:^16}|
|_____|____________|_________________________________________|________________|
|     |            |                                         |                |
|{:^5}|{:^12}|{:^41}|{:^16}|
|_____|____________|_________________________________________|________________|
|     |            |                                         |                |
|{:^5}|{:^12}|{:^41}|{:^16}|
|_____|____________|_________________________________________|________________|
|     |            |                                         |                |
|{:^5}|{:^12}|{:^41}|{:^16}|
|_____|____________|_________________________________________|________________|
|     |                                                                       |
|     |                                               Total Marks - {}       |
|     |                                               Percentage  - {:.2f}     |
|     |                                               Result - PASS           |
|_____|_______________________________________________________________________|'''
.format("Marksheet",Full_Name,Father_Name,Roll_No,Course_Name,
        "S No.","Subject Code","Subject Name","Marks",
        "1.","BT401","Mathematics-III",Subj1,
        "2.","CS402","Analysis Design Of Algorithm",Subj2,
        "3.","CS403","Software Engineering",Subj3,
        "4.","CS404","Computer Org. & Architecture",Subj4,
        "5.","CS405","Operating Systems",Subj5,
        Total_Marks,Percentage))