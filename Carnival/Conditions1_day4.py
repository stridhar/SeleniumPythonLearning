"""
#User input
num1 = int(input("Enter a number: "))
num2 = int(input("Enter 2nd number: "))
print(num1+num2)
#or
#print(int(num1)+int(num2))
"""
#Conditions
marks = int(input("Enter your marks: "))
if marks < 35:
    print("Fail")
elif marks >= 35 and marks < 45:
    print("Pass class")
elif marks >= 45 and marks < 60:
    print("second class")
elif marks >= 60 and marks < 85:
    print("First class")
elif marks >= 85 and marks < 100:
    print("Distinction class")
else:
    print("Contact admin")
