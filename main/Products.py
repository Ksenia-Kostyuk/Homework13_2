class Product:
    """Описание конкретного товара"""

    def __init__(self, name, description, price, remain):
        self.name = name
        self.description = description
        self._price = price
        self.remain = remain

    def __str__(self):
         return f'{self.name}, {self.price}. Остаток: {self.remain} шт.'

    def __add__(self, other):
        return self.price * self.remain + other.price * other.remain

    @classmethod
    def new_product(cls, name, description, price, remain):
        cls.new_product = name, description, price, remain
        return cls(dict(name=name, description=description, price=price, remain=remain))

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if int(new_price) <= 0:
            print(f'Цена введена некорректно')
        else:
            self._price = new_price
