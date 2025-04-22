from lib2to3.btm_matcher import type_repr

age = 37
weight = 76.5
name = "Aman"
address = "Azadpur, Delhi"
haveHome = True
fruites = ["apple", "Mango","Banana"]
subjects = {"Math", "Physics", "Chemistry"}
full_address = { "street" : "32-B",
                 "street2": "rameshwar nagar",
                 "city": "Delhi"}


print(age , " is ", type(age),".")
print(weight , " is ", type(weight),".")
print(name , " is ", type(name),".")
print(address , " is ", type(address),".")
print(haveHome," is ", type(haveHome),".")
print(fruites," is ", type(fruites),".")
print(subjects," is ", type(subjects),".")
print(full_address," is ", type(full_address),".")

print("----------------------------")

x = 10 # public variable
_x = 20 # protected variable
__x = 30 # private variable

print(type(x))
print(type(_x))
print(type(__x))


