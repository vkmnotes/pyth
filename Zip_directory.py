import zipfile
import os
with zipfile.ZipFile("archive.zip","w") as z:
    z.write("sample.txt")
    z.write("sample_copy.txt")
print("Files zipped into archive.zip")
with zipfile.ZipFile("archive.zip","r") as z:
    z.extractall("extracted_files")
print("Files unzipped into 'extracted_files' folder")
print("\nListing files and directories in current folder:")
for x in os.listdir("."):
    if os.path.isdir(x):
        print("Directory:",x)
    else:
        print("File:",x)
