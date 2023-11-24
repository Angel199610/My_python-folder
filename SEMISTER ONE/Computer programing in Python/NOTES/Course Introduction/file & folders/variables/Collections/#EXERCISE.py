#EXERCISE
#Change item value
student_marks = ([90, 85, 75, 69,])
student_marks[1] = ([89])
#print(student_marks)

student_marks = ([90, 85, 75, 69,])
student_marks[3] = ([55])
#print(student_marks)

#adding a value item
student_marks = ([90, 85, 75, 69,])
student_marks.append(69)
print(student_marks)

#find the size of item
student_marks = ([90, 85, 75, 69,])
print(len(student_marks))

#write a phython program to sum all item in the list
student_marks = ([90, 85, 75, 69,])
import math
student_marks = math.fsum([90, 85, 75, 69])
#print(student_marks)

#write a python that takes two lists and returns true if they have atleast one common member
student_marks = ([90, 85, 75, 69,])
list_1 = input("Enter items:")
list_2 = input("Enter items:")
if 85 in student_marks:
    print ("true 69, 85, 90 common number")
else: 
    print("false 85 does not exist")
    
#find the size of the list having appended item 55
student_marks = ([90, 85, 75, 69,])
print(len(student_marks))
