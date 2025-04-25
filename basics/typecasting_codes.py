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
