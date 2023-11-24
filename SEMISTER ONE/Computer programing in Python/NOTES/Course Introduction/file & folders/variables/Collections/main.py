#creating a list that stores student marks
student_marks = ([90, 85, 75, 69,])
print(type(student_marks))
print(student_marks)
#accesing the positive index 
print(student_marks[3])
#Negative indexing
print(student_marks[-3])
#List slicing
print(student_marks[1:2])
print(student_marks[0:3])
print(student_marks[0:5])

#check if item exists
student_marks = ([90, 85, 75, 69,])
if 85 in student_marks:
    print("yes 80 is in the list")
else:
    print("no 80 does not exist")

#write aphython program to sum all item in the list
student_marks = ([90, 89, 75, 69, 55])


#write a python that takes two lists and returns true if they have atleast one common member
#find the size of the list having appended item 55