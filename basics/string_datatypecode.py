'''
STRING : any sequence of character within single or double quotes.
1. there are two type of literals, Single line and multi-line.
2. Single line literals use, Single or double quotes.
3. For multi-line literals , use triple quotes.

'''

multiline_str = '''Hello,
Umakant, How are you?
Hope you are good...!'''
print(multiline_str)

str1 = 'hello'
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[-1])
print(str1[-2])

print("Length of str1 is : ", len(str1))

# slice in string : it's operator. [] to retrieve the slice of string.
para1 = " logs collected at /mnt/logs/postgres/consents/file1.log find logs and check the issues."
para2 = " logs collected at /mnt/logs/snowflake/consents/file2.log find logs and check the issues."

log_start_index = para1.index("/mnt/logs/")
log_end_index = para1.index('.log')
print(para1[log_start_index:log_end_index+4])
print(para2[para2.index("/mnt/log"):para2.index(".log")+4])
