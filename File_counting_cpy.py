with open("sample.txt","r") as f:
    content=f.read()
print("Lines:",len(content.splitlines()))
print("Words:",len(content.split()))
print("Characters:",len(content))
with open("sample.txt","rb") as f:
    data=f.read()
with open("sample_copy.txt","wb") as f:
    f.write(data)
print("\nFile copied successfully.")
with open("sample_copy.txt","r") as f:
    print("Copied file content:")
    print(f.read())
