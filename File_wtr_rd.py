with open("sample.txt","w") as f:
    for i in range(1,6):
        f.write(f"This is line {i}\n")
with open("sample.txt","r") as f:
    print("File content:")
    print(f.read())
