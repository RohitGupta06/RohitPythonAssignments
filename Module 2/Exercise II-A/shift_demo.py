""" Write a program to show how shifting an integer left by one can be used to 
perform multiplication by two and how shifting an integer right by one can be 
used to perform division by two. """

# Taking inputs from user
Num = int(input("Enter the value of operand: "))
Bits_to_be_shifted = int(input("Enter the number of bits to be shifted: "))

# Selecting what to do
print("\nWhat would you like to do?")
print("1. Left Shift")
print("2. Right Shift")
choice = int(input())

# Performing Operations
if choice == 1:
    print("          MANUALLY")
    print(Num,"<<", Bits_to_be_shifted,"=", Num<<Bits_to_be_shifted)
    print("          USING FORMULA")
    LS = Num * (2 ** Bits_to_be_shifted)
    print(Num,"<<", Bits_to_be_shifted,"=",LS)
    print("So we can conclude that shifting an integer left by one can be used \
          to perform multiplication by two")
    
elif choice == 2:
    print("          MANUALLY")
    print(Num,">>", Bits_to_be_shifted,"=", Num>>Bits_to_be_shifted)
    print("          USING FORMULA")
    RS = Num // (2 ** Bits_to_be_shifted)
    print(Num,">>", Bits_to_be_shifted,"=",RS)
    print("So we can conclude that shifting an integer right by one can be used \
          to perform division by two")