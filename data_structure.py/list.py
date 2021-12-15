#initalize a list (linkedlist)
student_names = ["Mike", "Amy", "Charlie", "Marco", "David", "Leon", "Rain", "Angelina", "Yujing", "Henry", "Barbie", "Johnathan"]

#add a name to our list
student_names.append("Mars")
student_names.insert(0, "Mr. Amini") #insert at index (0) first position

#delete a name
student_names.remove("Charlie")

#iterate over our list
for name in student_names:
    print(name)

#get the length of the list
length = len(student_names)
print(length)

#sort list using built in list method .sort
student_names.sort()
for name in student_names:
    print(name)
    
#Character (letter) list
letter_grades = ["A", "A-", "A", "B", "B", "C", "C-", "A-", "B+"]
letter_grades.append("B")
letter_grades.append("A")
letter_grades.append("A")

#count number of people with grade A 
number_of_A_grades = letter_grades.count("A")
print("number of grades A:", number_of_A_grades)

#integer list
numbers = [0, 0, 1, 1, 2, 3, 4, 0, 0, 1, 1, 0, 0, 1, 0, 0]
zero_frequency = numbers.count(0)
print("number of zeros", zero_frequency)

#boolean list
has_completed_homework = [True, True, False, True, False, False, True]
number_of_completed_homeworks = has_completed_homework.count(True)
print("Number of people who did homework", number_of_completed_homeworks)








#create a list of boolean values to represent 
# students who has done their homework 
has_done_homework = [True, False, True, False, True, False, False, True]
print(has_done_homework)
has_done_homework.sort()
print(has_done_homework)

#how many false values are in this data structure ?
number_False = has_completed_homework.count(False)
print(number_False)

#interate (traverse the data structure)
for student in has_completed_homework:
    print(student)

#make a list that stores the amount of money has in their pocket
money_in_student_pockets = [50, 10, 94, 100, 250, 36.5, 3000]

#sort the money in increasing order
money_in_student_pockets.sort()
print(money_in_student_pockets)
#sort the money in increasing order 
money_in_student_pockets.sort()
print(money_in_student_pockets)
#add
money_in_student_pockets.append(34)
print(money_in_student_pockets)


#create a list of strings
student_names = ["Adrian", "Mike", "Charlie", "Hanson", "Barbie"]
print(student_names)
student_names.sort()
print(student_names)