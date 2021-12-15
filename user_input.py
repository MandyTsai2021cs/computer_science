#variable to store user input
name = input("Enter yoyr name: Mandy ")

#output the user input on the screen
print("Good morning",name)




#ask user to enter a number(interger)
#save it in a variable called "number"
number = int(input("Enter a number:"))


#pass input to a function that does math
def get_square (number):
    return number * number


#call the square function, pass "number" as argument
#ave the result in a variable called "square"
#print the "square" variable on screen
square = get_square (number)
print(square)
