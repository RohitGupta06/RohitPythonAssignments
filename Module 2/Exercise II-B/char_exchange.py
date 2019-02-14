# Taking the string input from user
user_input = input("Please enter your string: ")

# Exchanging First and Last Character
length = len(user_input)
updated_string = user_input[-1] + user_input[1:length-1] + user_input[0]
print("The updated string is",updated_string)