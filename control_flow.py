#program make decisions based on control logic (control flow)

student_grade = 93

if student_grade > 90:
    print("Your grade is A")
elif student_grade < 90 and student_grade > 80:
    print ("Your grade is a B")
elif student_grade < 80 and student_grade > 70:
    print ("Your grade is a C")
else:
    print("Your grade is a D or F")




#write a progrm using if-elif-else that...
#looks at a variable for temperature 
#if temperature is above 30 C,print it's hot 
#elif temperature is above 10 C, but below 30 C, print it's warm 
#elif temperature is below 10 C, print it's cold 
#else print "bring an umbrells just in case"

temperature = 20 

if temperature > 30:
    print("it's hot")
elif temperature < 30 and temperature > 10:
    print ("print it's warm")
elif student_grade < 10:
    print ("it's cold")
else:
    print("bring an umbrells just in case")




