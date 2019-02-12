# A five digit number is inputted through the keyboard. 
# Write a program to add 1 to each of its digit.
# For example, if number inputted is 45394 then the output will be 56405.

# Initializing variables
Sum = 0

# Taking input from the user
Num = int(input("Plz enter a 5 digit number: "))
Temp = Num

# Calculation
Mod = ((Temp // 10000) + 1) % 10
Sum = Sum + Mod * 10000

Mod = (((Temp // 1000) - ((Temp // 10000) * 10)) + 1) % 10
Sum = Sum + Mod * 1000

Mod = (((Temp // 100) - ((Temp // 1000) * 10)) + 1) % 10
Sum = Sum + Mod * 100

Mod = (((Temp // 10) - ((Temp // 100) * 10)) + 1) % 10
Sum = Sum + Mod * 10

Mod = (((Temp) - ((Temp // 10) * 10)) + 1) % 10
Sum = Sum + Mod * 1

# Displaying the result
print("The desired result is", Sum)