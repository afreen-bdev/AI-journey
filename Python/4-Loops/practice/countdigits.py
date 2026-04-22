num = 5463212345
count = 0

while num > 0:
    num //= 10
    count += 1

print("Digits:",count)