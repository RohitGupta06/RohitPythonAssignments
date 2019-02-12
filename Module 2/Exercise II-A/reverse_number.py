# A five digit number is inputted from the keyboard.
# Write a program to reverse the number.

# Initializing variables
Sum = 0

# Taking input from the user
Num = int(input("Plz enter a 5 digit number: "))
Temp = Num

# Calculation
Sum = Sum * 10 + (Temp % 10)
Temp = Temp // 10

Sum = Sum * 10 + (Temp % 10)
Temp = Temp // 10

Sum = Sum * 10 + (Temp % 10)
Temp = Temp // 10

Sum = Sum * 10 + (Temp % 10)
Temp = Temp // 10

Sum = Sum * 10 + (Temp % 10)
Temp = Temp // 10

# Displaying the reverse
print("Reverse of", Num, "is", Sum) 