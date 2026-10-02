dict1={"a":10,"b":20,"c":30}
dict2={"b":5,"c":15,"d":25}
merged=dict1.copy()
for k,v in dict2.items():
    merged[k]=merged.get(k,0)+v
print("Merged dictionary:",merged)
sentence="the quick brown fox jumps over the lazy dog the fox runs"
freq={}
for word in sentence.split():
    freq[word]=freq.get(word,0)+1
print("\nWord frequency:")
for word,count in freq.items():
    print(f"{word}: {count}")
