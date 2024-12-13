class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user):
        self.products = {}  # Зберігає товар та його кількість
        self.user = user

    def add_item(self, item, cnt):
        # Якщо товар уже є в замовленні, збільшуємо кількість
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def get_total(self):
        # Обчислюємо загальну вартість
        return sum(item.price * cnt for item, cnt in self.products.items())

    def __str__(self):
        items_str = "\n".join(f"{item.name}: {cnt} pcs." for item, cnt in self.products.items())
        return f"User: {self.user}\nItems:\n{items_str}\nTotal: {self.get_total()}"

# Тестування
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "0963495665")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
Total: 60
"""
assert isinstance(cart.user, User), 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 30 pcs.
Total: 80
"""
assert cart.get_total() == 80, 'Повинно залишатися 80!'
