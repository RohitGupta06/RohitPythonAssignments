# Taking input from user
path = input("Enter the path of file: ")

# Printing the extension of file
Temp = path.split("/")
Temp = Temp[-1]
Temp = Temp.split(".")
Temp[1] = ".pdf"
Extension = Temp[0] + Temp[1]
print("New Extension of the file is:",Extension)