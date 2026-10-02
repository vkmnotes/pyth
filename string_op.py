s=input("Enter a string: ")
s=s.lower().replace(" ","")
print("Palindrome" if s==s[::-1] else "Not a palindrome")
text=input("Enter another string: ")
vowels=consonants=digits=special=0
for c in text:
    if c.isalpha():
        if c.lower() in "aeiou":
            vowels+=1
        else:
            consonants+=1
    elif c.isdigit():
        digits+=1
    elif not c.isspace():
        special+=1
print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}, Special: {special}")
