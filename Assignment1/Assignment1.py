#6,8,12,13,14
# #Solution 1st
# def Breakdown(st):
#     """
#     >>> Breakdown("Vikas")   
#     ['V', 'i', 'k', 'a', 's']
#     """
#     return [char for char in st]

# #Solution 2nd
# def Collect(strg):
#    """
#    >>> Collect(['V', 'i', 'k', 'a', 's'])
#    'Vikas'
#    """
#    ns = ""
#    for i in strg:
#        ns += i
#    return ns

# #Solution 3rd
# def Random_num(n):
#    """
#    >>> Random_num(5)
#    """
#    import random
#    rn = [random.randrange(1,100,1) for i in range(n)]
#    return rn


# #Solution 4th
# def Des_sort(lst):
#     """
#     >>> Des_sort([1,2,3,4,5])
#     [5,4,3,2,1]
#     """
#     lst.sort(reverse = True)
#     return lst

 
# # Solution 5th
# def word_count(cs):  # it will count the frequency of a char in a string
#     """
#     >>> word_count([1,1,3,2,3,2,3,2,2])
#     {1: 2, 3: 3, 2: 4}
#     """
#     count={}
#     for i in cs:
#         count[i] = cs.count(i)
#     return count
 
    
# #Solution 6th
# def list_to_set(lst): 
#     """
#     >>> list_to_set([1, 1, 3, 2, 3, 2, 3, 2, 2])
#     {1, 2, 3}
#     """
#     return set(lst)
     
    

# #Solution 7th
# def first_repeat(ilst):
#     """
#     >>> first_repeat([1,2,3,4,5,1,2])
#     1
#     """
#     for i in range(len(ilst)):
#         if ilst.count(ilst[i]) > 1:
#             return ilst[i]



#solution 8th
def Sol8(n):
    """
    >>> Sol8(3)
    {
    0:[0,0],
    1:[1,1],
    2:[4,8],
    3:[9,27]
    }
    """
    dct = {}
    for i in range(0,n+1):
        value = [i**2,i**3]
        dct.update({i:value})
    return dct
     
    
       
        
        
# # Solution 9th
# def Zip_merge(lst1, lst2):
#     """
#     >>> Zip_merge([1,2,3,4], ['a','b','c','d'])
#     [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
#     """
#     lst3 = zip(lst1,lst2)
#     return lst3

 
 

# # Solution 10th
# def Squares(n):
#     """
#     >>> Squares(5)
#     [0, 1, 4, 9, 16]
#     """
#     return [i**2 for i in range(0,n)]


# Solution 11th
def Map_Dic(n):
    """
    >>> Map_Dic(5)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    """
    sqr = {i:i**2 for i in range(0,n+1)}
    return sqr

# #Solution 12th
# def sqr(x):
#     return x**2

# class MyClass:
#     def __init__(self,lst):
#         self.lst = lst       #instense variable

# c1 = MyClass([1,2,3,4])
# print(c1.apply(lambda x:x**2))


# #Soltion 13th
# def Upper_Case(lst):
#     """
#     >>> Upper_Case(['aa','bb','cd','e'])
#     ['AA', 'BB', 'CD', 'E']
#     """
#     return lst.upper()

# # Solution 14th
# def Multiply(lst):
#     """
#     >>> Multiply([1,2,3,4,5])
#     120
#     """
#     rst = functools.reduce(operator.mul,lst)
#     return rst
