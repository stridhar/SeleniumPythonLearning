#Slicing
para = "hello All WElcome To Learning pyThon selEnium"
print(para[0:20].upper())
print(para[0:20].upper(),para[20:])
print(para[0:20].upper(),para[20:].lower())  #Using , as concatenation
print(para[0:20].upper()+para[20:].lower())  #Using + as concatenation
print("----------------------------------------")
value = "Ganesh Holla"
print(value[0:3].upper()+value[3:])
print(value[0:3].upper()+value[3:].replace(" ",""))