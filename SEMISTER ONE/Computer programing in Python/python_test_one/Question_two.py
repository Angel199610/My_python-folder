# #Function to find th average of two numbers 
# def average_two (x, y):
#     x = 0
#     y = 5
#     average = (x + y)/2
#     return average


# #Test the program with 2 different numbers 
# x = 5
# y = 20
# result = average_two(x, y)
# print(f"The Average of x and Y is:",{result})


# #A program that asks the user to input 3 numbers and find minimum number
# list_1 = float (input("Enter Your first number: "))
# list_2 = float (input("Enter Your Second number: "))
# list_3 = float (input("Enter Your third number: "))
# minimum_number = min(list_1, list_2, list_3)
# print(f"The Minimum number of the test is: ", {minimum_number})

# #corrections
# def average (x, y):
#     sum = x + y
#     average_score = sum / 2
#     print(f"Average score is {average_score}")
# average (90, 88)

#Finding the mininmum number
# def minimum_number (a, b, c):
#     a = int(input("Enter the first number"))
#     b = int(input("Enter your second number"))
#     c = int(input("Enter Your third number"))
#     if (a<b and a<c):
#         print(f"{a} is the minimum number")
#     elif(b<c and b<c):
#         print(f"{b} is the minimum number")
#     else:
#         print(f"{c} is the minimum number")
# minimum_number (80, 90, 75,)

#Question 3
[90, 88, 84, 71, 49]

python = 90
Machine_learning = 88
mathematical_computing = 84
Graphics = 71
Career_guidance = 49
print(f"Python marks = {python}")
print(f"Machine Learning marks = {Machine_learning}")
print(f"Graphics marks = {Graphics}")
print(f"Career Guidance  marks {Career_guidance}")

def grade_course_unit(mark):
    if (mark >= 90 and mark <= 100):
        
        print(f"You scored an A")
    elif (mark>=80 and mark <= 89):
        print(f"You scored a B")
    else:
        print(f"You have really failed")
grade_course_unit(90)