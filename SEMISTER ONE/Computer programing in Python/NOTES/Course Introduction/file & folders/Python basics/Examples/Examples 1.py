#Write a python program that counts the total numbers of even numbers and odd numbers in this tuple
#(1,2,3,4,5,6,7,8)
# Numbers = (1,2,3,4,5,6,7,8)
# for a in Numbers:
#     if a % 2 == 0:
#         print(a, end= " ")

# Numbers = (1,2,3,4,5,6,7,8)
# count_even = 0
# count_odd = 0
# for a in Numbers:
#     if a % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1
#         print(f"even numbers {count_even} and odd numbers {count_odd}")

# data = (1,2,3,4,5,6,7,8)
# def count_even_numbers (data):
#     count_even = 0
#     count_odd = 0
#     for a in data:
#         if a % 2 == 0:
#              count_even += 1
#         else:
#              count_odd += 1
#     print(f"{count_even} and {count_odd}")


# numbers = (1, 2, 3, 4, 5, 6, 7, 8,) # Declaring the tuple
# count_odd = 0
# count_even = 0
# for x in numbers:
# 	if not x % 2:
# 		count_even+=1
# 	else:
#     	     count_odd+=1
# print("Number of even numbers :",count_even)
# print("Number of odd numbers :",count_odd)


# #Create a program that returns the sum for the multiples of seven and five numbers (1,7,20,35,49,50)
Numbers = (1,7,20,35,49,50)
def sum_of_multiples_of_seven_and_five(data):
           sum_of_multiples_of_seven = 0
           sum_of_multiples_of_five = 0
           for a in data:
                  if a % 5 == 0:
                         sum_of_multiples_of_five += a
                  if (a % 7 == 0):
                         sum_of_multiples_of_seven += a
                         print(f"{sum_of_multiples_of_five}, {sum_of_multiples_of_seven}")                       




