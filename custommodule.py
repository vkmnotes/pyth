import mymath
num=17
if mymath.is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")
def student_details(name,age=18,grade="A"):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")
student_details("Alice")
student_details("Bob",age=20,grade="B")
student_details(name="Charlie",grade="A+")
