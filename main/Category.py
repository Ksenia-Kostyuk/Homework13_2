from main.Products import Product

class Category:
    """Описание категории товаров"""
    name = str
    description = str
    __products = list
    sum_products = 3
    unique_product = 1

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products


    def __len__(self):
        return len(self.__products)


    def __str__(self):
        return f'{name}, количество продуктов: {len(self.__products)}'


    def get_products(self):
        for i in self.__products:
            return (f'Продукты:\n{i['product']}, {i['pay']}, остаток {i['remains']}')

    def set_new_product(self, new_product):
        self.__products.append(new_product)
