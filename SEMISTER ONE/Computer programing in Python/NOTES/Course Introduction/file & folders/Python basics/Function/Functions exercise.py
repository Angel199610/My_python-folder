
#Write a python function to sum all the  number in a list 
#sample list (8,2,3,0,7)
#solution
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))

#Write a python function to reverse a string ("1,2,3,4,5,a,b,c,d")



#Write a python program to mulitplying all numbers in the list (8,2,3,-1,7)
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))




#Write a pythoin program to print the even number from a given list (1,2,3,4,5,6,7,8,9)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def get_evens(input_list):
    output = [x for x in input_list if x % 2 == 0]
    return output
print(get_evens(list1))