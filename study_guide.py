#1 variable - 
#a) Write a boolean to represent whether or not you will pass the exam 
passed_exam = True

#b) Write an interger variable to represent your score on the exam
my_score = 90 

#c) Write a floating point variable to represent the class average on the exam
class_average = 85.5

#d) Write a string variable to represent something you'd say to your friend in the morning
message = "good_morning"

 #2 iterations - for loops
 #a) write a for loop that print "I am a polite and kind person" 10x
 for i in range(10):
     print("I am a polite and kind person", i)

#control flow - write a simple if-elif statement to describe this..
#a) if student has a grade of 90-100 print "you rock"
#b) elif student has a grade of 80-90 print "you are great"
#c) elif student has a grade of 70-80 print "not bad, keep working"
#d) elif student has a grade less than 70 print "keep working champ"
#> < >= and or not if-elif-else
student_grade = 77

if student_grade > 90 and student_grade <= 100:
    print("you're a rockstar student")
elif student_grade > 80 and student_grade <= 90:
    print("you're amazing, keep leveling up")
elif student_grade > 70 and student_grade <= 80:
    print("you're amazing, keep leveling up")

