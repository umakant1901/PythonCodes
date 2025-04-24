'''
COMPLEX DATA TYPE:

"i + cj;" is type of complex data type.

i is real part. => it can be of any base type.
c is imaginary part. => it should be decimal or float
j is fixed part.

2. real and imag are the key/variable to get complex number's real and imaginary number.

'''
complex_num = 2+5j
print(complex_num)
print(type(complex_num))
print("***************")
complex_num1 = 2.5+5.5j
print(complex_num1)
print(type(complex_num1))

print(complex_num + complex_num1)
print(complex_num * complex_num1)
print("***************")

print(complex_num1.real , complex_num1.imag)
