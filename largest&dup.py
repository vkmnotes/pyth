numbers=[23,45,12,67,34,89,2]
largest=second=float("-inf")
for n in numbers:
    if n>largest:
        second,largest=largest,n
    elif n>second and n!=largest:
        second=n
print("Largest:",largest)
print("Second Largest:",second)
lst=[1,2,2,3,4,4,5,1]
print("List without duplicates (order preserved):",list(dict.fromkeys(lst)))
