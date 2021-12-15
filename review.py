#data types 
#1 write a variable that stores a boolean 
is_prepares_for_class = True
pays_attention_in_class = False
sleeps_in_class = False

#2 write a variable that store an integer
class_average = 88

#3 write a variable that stores a floating point number 
height = 160.6

#loops
#1. write a for loop that sys "happy birthday Barbie + Howard" 12x
for i in range(12):
    print("happy birthday Barbie + Howard")

#while loop
#1. write a while loop to print ("goodmorning") 4x

count = 0
while(count < 4):
    print("goodmorning")
    count = count + 1 

#functions
def addition(number, another_number):
    return number + another_number

print(addition(10,10))

#random 
import random
random_number = random.randint(1,99)
print(random_number)



