class Product:
    """Описание конкретного товара"""
    name = str
    description = str
    _pay = int
    remain = int

    def __init__(self, name, description, pay, remain):
        self.name = name
        self.description = description
        self._pay = pay
        self.remain = remain


    def __str__(self):
         return f'{self.name}, {self.pay}. Остаток: {self.remain} шт.'


    def __add__(self, other):
        return self.pay * self.remain + other.pay * other.remain


    def new_product(self, product, description, pay, remain):
        used_product = {}
        used_product['product'] = product
        used_product['description'] = description
        used_product['pay'] = pay
        used_product['remain'] = remain
        return used_product


    def set_pay(self, new_pay):
        if new_pay <= 0:
            print (f'Цена {new_pay} введена некорректно')
        else:
            self._pay = new_pay
