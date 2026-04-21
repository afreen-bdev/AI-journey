with open("sample.txt", "r") as src:
    data = src.read()

with open("copy.txt", "w") as dest:
    dest.write(data)

print("File copied successfully")