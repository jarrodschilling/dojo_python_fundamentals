from products import Product

class Store():
    def __init__(self, name):
        self.name = name
        self.products_list = []
    
    def add_product(self, new_product):
        self.products_list.append(new_product)
        return self
    
    def sell_product(self, id):
        self.products_list.pop(id)
        return self
    
    def inflation(self, percent_increase):
        for product in self.products_list:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for product in self.products_list:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self









