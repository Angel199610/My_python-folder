# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# common_member=[]
# for i in range(len(a)):
#     if a[i] in b:
#         common_member.append(a[i])
# c=set(common_member)
# print(c)

# a = [1, 2, 3, 4, 5]
# b = [5, 6, 7, 8, 9]
# common_member = []
# if a.intersection b
# print(common_member(a, b))


import operator as op
def common_member(a, b):
    result = [i for i in a if op.countOf(b,i)>0 ]
    return result
 
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
 
print("The common elements in the two lists are: ")
print(common_member(a, b))
          