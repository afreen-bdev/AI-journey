# Practice — custom module usage
from utils import add, multiply

print(add(10, 5))
print(multiply(4, 6))

# __name__ usage
def test():
    print("Running test function")

if __name__ == "__main__":
    test()