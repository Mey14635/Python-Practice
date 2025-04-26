normal_string=input("enter a string: ")  #receive the input from user
opposite_string=""  #A empty string  will store the new reverse words
for letter in normal_string: #ie for each letter put it in front of the current opposite_string
    opposite_string=letter+opposite_string #the new letter will push the existing forward as the loop is repeating
print(f"Reverse of string is : {opposite_string}")