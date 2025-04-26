'''
Method of type casting:
1.  int()   : from other type to int.(apart from complex)
2.  float()
3.  complex()
4.  bool()
5.  str()

'''
float_num = 123.34
int_str = '321'
float_str = '123.45'
print(int(float_num))
print(int(int_str))
# print(int(float_str))  # ValueError: invalid literal for int() with base 10: '123.45'
print('**************************')
print(float(10))
print(float(True))
print(float('11'))
print(float('12.12'))
print(float(False))
print(float(0b101010))
print('**************************')

print(bool('1'))
print(bool('0'))
print(bool('123'))
print(bool(1))
print(bool(0))
print(bool())

print('**************************')
print('Single Argument ==>')
print(complex(2))
print(complex(3.3))
print(complex('4'))
print(complex(True))
print(complex(False))
print(complex('2+4j'))

print('Two argument Complex convertion ==>')
print(complex(1,2))
print(complex(3.3,4.4))
# print(complex('5.5',6.6)) #TypeError: complex() can't take second arg if first is a string
# print(complex(7,'7.7')) # TypeError: complex() second arg can't be a string
print(complex(True, True))
print(complex(False, False))