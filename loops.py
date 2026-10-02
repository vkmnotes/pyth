num=int(input("Enter a number for table: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
print("\nPrime numbers between 1 and 50:")
for n in range(2,51):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    else:
        print(n,end=" ")
print("\n\nEven numbers from 1 to 20 (using continue):")
for n in range(1,21):
    if n%2:
        continue
    print(n,end=" ")
print()
