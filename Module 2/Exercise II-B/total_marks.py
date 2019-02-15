# Marksheet

# Taking Marks obtained by student
Marks = input("Enter the Marks: ").split(",")

# Calculating Total Marks and Percentage
Total = (int(Marks[0]) + int(Marks[1]) + int(Marks[2]) + int(Marks[3]) 
+ int(Marks[4]) + int(Marks[5]) + int(Marks[6]) + int(Marks[7]))
Percentage = (Total/440) * 100

# Displaying Total Marks and Percentage
print("Total Marks obtained =",Total)
print("Percentage obtained =",Percentage)