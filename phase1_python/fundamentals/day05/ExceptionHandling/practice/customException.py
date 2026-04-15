def withdraw(balance, amount):
    if amount > balance:
        raise Exception("Insufficient balance")
    return balance - amount

try:
    print(withdraw(1000, 1500))
except Exception as e:
    print(e)