class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title} costs {self.price}"

b = Book("Python", 500)
print(b)