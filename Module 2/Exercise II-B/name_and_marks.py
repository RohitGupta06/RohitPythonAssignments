# Marksheet

# Taking Marks obtained by student
Marks = input("Enter the Name and Marks: ").split(",")

# Calculating Total Marks and Percentage
Total_Theory_Marks = (int(Marks[1]) + int(Marks[2]) + int(Marks[3]) + int(Marks[4]) + int(Marks[5]))
Total_Practical_Marks = (int(Marks[6]) + int(Marks[7]) + int(Marks[8]))
Percentage = ((Total_Theory_Marks + Total_Practical_Marks)/440)*100

# Printing the result introduction statement
print(Marks[0],"obtained",Total_Theory_Marks," marks out of 350 in Theory and",
      Total_Practical_Marks,"marks out of 90 in Practical and successfully passed the exam with",
      Percentage,"in aggregate. Many congratulation to",Marks[0],".")