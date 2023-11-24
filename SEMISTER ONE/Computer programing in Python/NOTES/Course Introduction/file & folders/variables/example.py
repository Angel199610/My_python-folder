#A python program that takes in the student name and class

Name_of_the_student = input("enter your name:")
Student_class = input("enter your class:")
Student_section = input("enter your Section:")

#Subjects and their marks (We use float to)
Excel_mark = float(input("enter your Excel scored:"))
Html_mark = float (input("enter your Html scored:"))
Java_mark = float (input("enter your Java mark scored:"))
python_mark = float(input("enter your python mark scored:"))
PHP_mark = float(input("enter your PHP mark scored:"))
Total_marks = (Excel_mark + Html_mark + Java_mark + python_mark + PHP_mark)
percentage = (Total_marks)/5
# print(Name_of_the_student)
# print(Student_class)
# print(Student_section)
# print(Total_marks)
# print(percentage)
print("Dear {Name_of_the_student} you are in {Student_class}, your percentage mark is {percentage//}")