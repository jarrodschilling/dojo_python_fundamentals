from store import Store
from products import Product

lululemon = Store("lululemon")

abc = Product("abc", 130, "pants")
commission = Product("commission", 140, "pants")
metal_vent = Product("metal_vent", 70, "shirt")
evolution = Product("evolution", 90, "shirt")

lululemon.add_product(abc).add_product(evolution).set_clearance("pants", 0.1)

print(lululemon.products_list)