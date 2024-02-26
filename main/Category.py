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


    def get_products(self):
        for i in self.__products:
            return (f'Продукты:\n{i['product']}, {i['pay']}, остаток {i['remains']}')

    def set_new_product(self, new_product):
        self.__products.append(new_product)



if __name__ == '__main__':
    name = Category('Фрукты', 'Сладкое', [{'product': 'Яблоко', 'pay': 10.0, 'remains': 3}])
    op = Product('Яблоко', 'Сладкое', 10, 3)
