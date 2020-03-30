#replace
value="1abc2abc3abc4abc"
print(value.upper())
print(value.replace('abc','EFG'))
#i don't want to replace all the string, want to replace first 2 abc only
print(value.replace('abc','EFG',2))

#capitalize
para = "hello All WElcome To Learning pyThon selEnium"
print(para)
print(para.capitalize())

#Finding count using the length
print("Total no of chars: ",len(para))

#Print reverse order
value="1234567890"
print(value[::-1])