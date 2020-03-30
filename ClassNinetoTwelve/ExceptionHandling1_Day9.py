print("starting.......")
try:
    i=10
    z=0
    print(i/z)
except ZeroDivisionError:
    print("Zerodivision exception occured")
except FileNotFoundError:
    print("FileNotFound exception occured")
else:
    print("Exception not occured")
finally:
    print("Mandatory execution")
print("ending.......")