'''
LIST:

1. Maintain order of element. means preserve the element in sequence.
2. Represented with [].
3. Used for heterogeneous data
4. Duplicate values allowed.
5. Indexing and slicing are allowed.
6. Growable in nature. Add element using "append()".
7. List is mutable.

CASE : if content is not fixed and keep on change : use list
i.g. Comment on social sites
'''

list1 = ["Milk" , 29 , "Crud", 23.45 , True , 2+3j , False]
print(list1)
print(list1[2])
print(list1[3:8])
print(list1[-1])
list1.append("Extra")
list1.append("Data")
print(list1)
list1.pop(4)
print(list1)
list1.remove("Crud")
print(list1)

lst = [2,4,6,8]
cp_lst = lst
print(lst)
print(cp_lst)
print(id(lst))
print(id(cp_lst))
lst[0]= 1
print(lst)
print(cp_lst)
print(id(lst))
print(id(cp_lst))
cp_lst[3]=7
print(lst)
print(cp_lst)
print(id(lst))
print(id(cp_lst))
