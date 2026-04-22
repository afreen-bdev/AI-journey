# Day 02 — Loop Concepts

# for loop
print("For Loop Example:")
for i in range(1, 6):
    print(i)

# while loop
print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print(count)
    count += 1

# break example
print("\nBreak Example:")
for i in range(10):
    if i == 5:
        break
    print(i)

# continue example
print("\nContinue Example:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# nested loop
print("\nNested Loop Example:")
for i in range(3):
    for j in range(3):
        print(i, j)