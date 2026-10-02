def calculate_area(l,w):
    return l*w,2*(l+w)
a,p=calculate_area(5,3)
print(f"Area: {a}, Perimeter: {p}")
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)
num=int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
square=lambda x:x**2
print("Square of 6:",square(6))
pairs=[(1,'b'),(3,'a'),(2,'c')]
print("Sorted by second element:",sorted(pairs,key=lambda x:x[1]))
