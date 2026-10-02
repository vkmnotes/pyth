lst=[10,20,30,40,50,60]
print("Original list:",lst)
print("Reversed:",lst[::-1])
print("Every second element:",lst[::2])
person=("Alice",25,"Engineer")
name,age,profession=person
print(f"\nName: {name}, Age: {age}, Profession: {profession}")
try:
    person[0]="Bob"
except TypeError as e:
    print("Error (tuples are immutable):",e)
