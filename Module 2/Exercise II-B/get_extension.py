# Taking input from user
path = input("Enter the path of file: ")

# Printing the extension of file
Temp = path.split(".")
Extension = Temp[1]
print("Extension of file is",Extension)