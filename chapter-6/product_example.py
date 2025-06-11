#!/usr/bin/env python3

class Product:
    def __init__(self,name,price):
        self._name = name
        self._price = price

    def describe(self):
        return f"General Product: {self._name} {self._price}"
    

class Book(Product):
    def __init__(self,name,price,author):
        self._name = name
        self._price = price
        self._author = author

    def describe(self):
        return f"Book: {self._name}, {self._price}, {self._author}"
    

class Electronics(Product):
    def __init__(self,name,price,brand):
        self._name = name
        self._price = price
        self._brand = brand

    def describe(self):
        return f"Electronics: {self._name}, {self._price}, {self._brand}"
    

class Service(Product):
    def __init__(self,name,price,validity):
        self._name = name
        self._price = price
        self._validity = validity

    def describe(self):
        return f"Service:{self._name}, {self._price}, {self._validity}"
    

def display_list_of_products(products):
    for product in products:
        print(product.describe())



def main():
    book = Book("Thinking fast and slow",18,"Daniel Kahneman")
    phone = Electronics("Phone Pro Max","1500","Orange")
    support_plan = Service("Extended Warranty",100,"2 Years")
    general_item = Product("Prepaid Card",150)
    product_list = [book,phone,support_plan,general_item]
    display_list_of_products(products=product_list)

if __name__ == "__main__":
    main()
