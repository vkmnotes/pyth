num=float(input("Enter a number: "))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")
age=int(input("Enter age: "))
assert age>=0,"Age cannot be negative!"
print("Valid age:",age)
