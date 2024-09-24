from pprint import pprint


class Product:

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        info = file.read()
        file.close()
        return info

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for i in products:
            if str(i) not in Shop.get_products(self):
                file.write(f'{i}\n')
            else:
                print(f'Продукт {str(i)} уже есть в магазине\n')
        file.close()

shop1 = Shop()
product1 = Product('Potato', 50.5, 'Vegetables')
product2 = Product('Spaghetti', 3.4, 'Groceries')
product3 = Product('Potato', 5.5, 'Vegetables')

print(product2)  # __str__
shop1.add(product1, product2, product3)

print(shop1.get_products())
