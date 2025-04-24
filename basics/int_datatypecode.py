name = "Ram"

 # Most common methods used in python
print(name) # to print value of object
print(type(name)) # to print the type of object
print(id(name)) # to print the id/address of object

# int data type
age = 30
weight = 76.50
mobile = 123456909876543
print(age, " is type of : ", type(age))
print(weight, " is type of : ", type(weight))
print(mobile, " is type of : ", type(mobile))

'''
we can represent int value in multiple ways:
1. decimal (base - 10) , allowed values : 0 - 9
2. binary (base - 2) , allowed values : 0 and 1
3. octal (base - 8) , allowed values : 0 - 7
4. hexadecimal (base - 16) , allowed values : 0 - 9 and A-F 

Base conversion function: number convert into  method type from any number of type.
bin()   ,   oct()   ,   hex()

'''

decimal_int = 10 # no prefix
print(decimal_int)

binary_int = 0B10 # 0b or 0B is prefix
print(binary_int)

octal_int = 0o10 # 0o or 0O is prefix
print(octal_int)

hexa_int = 0x10 # 0x or 0X is prefix
print(hexa_int)

# convert above numbers into all other type of number
# into binary
print(bin(decimal_int))
print(bin(octal_int))
print(bin(hexa_int))
print("**********")
# into octal
print(oct(decimal_int))
print(oct(binary_int))
print(oct(hexa_int))
print("**********")
print(hex(decimal_int))
print(hex(binary_int))
print(hex(octal_int))





