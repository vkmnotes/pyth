import pickle
data={"name":"Alice","age":25,"city":"Pune"}
with open("data.pkl","wb") as f:
    pickle.dump(data,f)
with open("data.pkl","rb") as f:
    print("Loaded data using pickle:",pickle.load(f))
with open("sample.txt","rb") as f:
    print("\nInitial position:",f.tell())
    print("Read data:",f.read(10))
    print("Position after read:",f.tell())
    f.seek(0)
    print("Position after seek(0):",f.tell())
