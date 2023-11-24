#Writing a tuples
marks = (80,79,69,70)
marks[0] 
print(type(marks))
print((len(marks)))
print(marks[0])

Marks = (80,) #Find the datatype
print(type(Marks))

# #Check whether 79 exists in the variable marks
marks = (80,79,69,70)
exist_count = marks.count(79)

if exist_count > 0:
    print("Yes, 79 exists in marks")
else:
    print("No, 79 does not exists in list")



# #Check whether 88 belongs to variable marks if it does not exist print 89
marks = (80,79,69,70) #first method
exist_count = marks.count(89)
if exist_count > 0:
    print("No, 89 does not exist in marks")
else:
    print("Yes, 89 exist in marks")

marks = (80,79,69,70)# Second Method
if 79 in marks:
    print("Yes if 79 is in marks")
else: # Else caters for the items that are not in the tuple
    print("88 does not exist in marks")

#Question 2
age = 1-18 ("Teen")
19-29 ("Youth")
30-45 ("Adult")
if (age <= 1 and age>= 18):
    print("You are a Teen")
else:
    (age>=19 and age<= 29)
    print("you are a youth")

list_age = (18)
name = ("Sanctuary")
print(f"Am {name} and I am {list_age}")


# #Modification off tuples
marks = (60, 79,69,70)
new_list = list(marks)
print(type(new_list), new_list)

#Changing the list
marks = (60, 79, 69, 70)
new_list = list(marks)
new_list[1] = 88
marks = tuple(new_list)
print(marks)

#Add 99 to the tuple
updated_marks = (60, 88, 69, 70)
updated_list_marks = tuple(updated_marks)
updated_list_marks = list(updated_marks)
updated_list_marks.append (99)
print(tuple(len(updated_list_marks)))

