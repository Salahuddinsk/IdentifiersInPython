"""
assingment= create a similar story to show the add update and delete in the list
"""

"""
Sister asked his brother to order some foods from zomato for Christmas Celebration 
"""

# at first the cart is empty
cart = []

# Sister asked to add one veg Burger to the empty cart
cart.append ("Veg Burger")
print (cart)

# Sister asked to add one Packet of Lays to the cart
cart.append ("Lays")
print (cart)

# Sister asked to add  french fries to the cart
cart.append ("French Fries")
print(cart)

# Sister asked to add One Large Sprite Can to the cart
cart.append("Large Sprite Can")
print(cart)

# Sister asked to add One Large Peri Peri Chicken Pizza to the Cart
cart.append("Large Peri Peri Chicken Pizza")
print(cart)

# Sister Asked What was the first Item  Added to the cart
print(cart[0])

# Sister Asked What was the Last item Added to the cart
print(cart[4])

# Sister Asked How many items are there in the cart
print(len(cart))

# Sister Asked to replace Large Peri Peri Chicken Pizza with Paneer Pizza
cart[4] = "Paneer Pizza" 
print(cart)

# Sister Asked to replace Large Sprite Can with Coca Cola
cart[-2] = "Coca Cola"
print(cart)

# Sister Asked to remove Lays from the cart
cart.remove ('Lays')
print(cart)

# Sister Asked to add One Cadbury Bar in the cart
cart.append ("Cadbury Bar")
print(cart)

# Sister Asked to remove the French Fries From the Cart
cart.pop(1)
print(cart)

# Sister Asked how many items are there in the cart
print(len(cart))
print(cart)

"""
"""