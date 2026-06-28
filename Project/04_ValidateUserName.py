# validate user input exercise
# 1. username is no more than 12 characters
# 2.username must not contain spaces
# 3.username must not contain digits


name= input("Please Enter Your Name:")

if len(name)>12:
   print("Your name cannot be greater than 12 letters")
elif not name.find(" ")==-1 :
   print("Your name must not contain any spaces")
elif not name.isalpha() :    #if spaces were allowed we might not have used that, we should have used "elif any(char.isdigit() for char in name): " intstead
   print("No numbers allowed")
else :
   print(f"Welcome {name}")
