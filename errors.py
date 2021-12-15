#user input errror - this throws an exception if a string is given by use
#age = int(input("Enter your age:"))
age = int(input("Enter your age:"))

#try catch block
try:
    age = int(input("Enter your age:"))
except ValueError as error:
    print("please enter a number only")
    #print(error)
    #print(type(error))
else:
    print("no exceptions were thrown, excute this")


#data validation - length check 
password_length = len(password)

if(password_lengh < 7 or password_lengh > 15 ):
    print("passwoord is updated")
else: print("password")