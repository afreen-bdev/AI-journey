with open("sample.txt", "r") as file:
    count = 0
    for line in file:
        count += 1

print("Total lines:", count)