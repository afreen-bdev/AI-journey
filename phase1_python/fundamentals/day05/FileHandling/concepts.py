with open("sample.txt","w") as file:
    file.write("Hello, this is python file handling\n")
    file.write("Second line\n")

with open("sample.txt","r") as file:
    content =file.read()
    print("file content:\n",content)

with open("sample.txt","a") as file:
    file.write("appended line\n")

with open("sample.txt","r") as file:
    for line in file:
        print("line:",line.strip())