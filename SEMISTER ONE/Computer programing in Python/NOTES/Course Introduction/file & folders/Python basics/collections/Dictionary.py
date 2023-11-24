#Dicitionary
#How to access keys (Keys are the variables on the left)
student = {
    "name": "Angel",
    "Age": 21,
    "address": "Kasangati",
    "Cohort": 3
}
print(type(student))
x = student.keys ()
print(x)

# #How to access or get item in dictionary
student = {
    "name": "Angel",
    "Age": 21,
    "address": "Kasangati",
    "Cohort": 3
}
x = student.get ("name")
print(x)

#How to change items in dictionary
student = {
    "name": "Angel",
    "Age": 21,
    "address": "Kasangati",
    "Cohort": 3
}
student["address"] = "Bweyogerere"
print(student)