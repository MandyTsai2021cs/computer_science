import random 

randon_number = random.randint(1,100)
print(randon_number)

#main function
def main_function()
    first_number = get_random(1, 100)
    second_number = get_random(101, 200)
    result = add(first_number, second_number)
    print(result)
    


#helper function (subroutine)
def get_random(start, end):
    randon_number  = random.randint(start, end)
    return random_number


#helper function #2 (subroutine)
def add (number, another_number):
    return number + another_number


#call our main function to start the program
main_function()