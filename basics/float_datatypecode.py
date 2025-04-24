'''
float data type:
1.  normal float number 123.45
2. exponential form / scientific notation
f1 = 1.23e3
f2 = 1.23E3
both are valid.


'''

weight= 123.45
weight2 = 123.45
weight3 = weight
weight4 = 12.12
print(weight)
print(type(weight))

print(id(weight))
print(id(weight2))
print(id(weight3))
print(id(weight4))

f1 = 1.23e3
f2 = 1.23E4

print(f1,f2)