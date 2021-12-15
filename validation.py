#data validation - admin password
admin_password = input ("enter your new password")
admin_password_length = len(admin_password)

if(admin_password_length >=6 and admin_password_length <= 12):
    print("password is update")
else:
    print("password must be 6 to 12 charactor")


 

    name = input("enter yourname: ")
    #check if user enters an empty string, out of range string

    name_length = len(name)

    if(name_length == 0):
        print("You cannot enter an empty name")
    elif(name_length < 3):
        print("Name must be more than three letters")
    elif(name_length > 25):
        print("Name must be less 25 characters")





#write a program that takes a new pet name and validates its length
# in other words, it prints an error message to the user if...
# the name is less than 2 chars and greater than 29 chars.
# 2 < name =< 20

#outline the steps - algorithm
#ask user for pet name, store it in a variable 
#use fn to get pet name length, store length in a new variable 
#validate - if-elif to print error messages if len is outside boundaries

#1. askuser for pet name
pet_name = input('Enter your pet name: ')

#2. ge pet name length
pet_name_length = len(pet_name)

#3. validate length + display message to user
if(pet_name_length ==0):
    print("You must enter something")
elif(pet_name_length < 2):
    print("Your pet must have a name with nore than 2 letters")
elif(pet_name_length >= 20):
    print("Enter a name that is less than or equal to 20 letters")



#validation task - write code that takes user input and validates its length
#ask the user for a restaurant name
#validate that the name is greater than 5 letters and less than 25 letters 

#1 - get name of restaurant
restaurant_name = input("Enter a restaurant name: ")
print(restaurant_name)

#2 - get length
restaurant_name_length = len(restaurant_name)
print(restaurant_name_length)

#3 - validation
if(restaurant_name_length == 0):
    print("You must enter something")
elif(restaurant_name_length < 5):
    print("You must enter a name with more than five letters")
elif(restaurant_name_length > 55):
    print("You must enter a name with less than 25 letters")























