# A five digit number is inputted through the keyboard. 
# Write a program to calculate sum of its digit.

# Initializing variables
Sum = 0

# Taking input from the user
Num = int(input("Plz enter a 5 digit number: "))
Temp = Num

# Calculation
Sum = Sum + (Temp % 10)
Temp = Temp // 10

Sum = Sum + (Temp % 10)
Temp = Temp // 10

Sum = Sum + (Temp % 10)
Temp = Temp // 10

Sum = Sum + (Temp % 10)
Temp = Temp // 10

Sum = Sum + (Temp % 10)
Temp = Temp // 10

# Displaying the result
print("The sum of digits of", Num, "is",Sum)