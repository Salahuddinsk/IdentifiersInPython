"""
Assignment do append and print using 'f' string

"""

"""
Mom asked me to add some items to the cart
"""
#  Initially we have an empty cart
cart = []

# Mom told me to add 2 packet of milk from the brand of amul in the empty cart
item = {
    'name' : 'Milk',
    'brand': 'Amul',
     'quantity': 2
}
cart.append(item)
print(cart)

# Mom asked me again to add 2 Packet of bread of Britannia to the cart
item = {
      'name': 'Bread',
      'brand': 'Britannia',
      'quantity': 2
}
cart.append(item)


# Mom asked me to add a 3 jar of Strawbery jams of Kissan to the cart
item= {
    'name':'Strawberry jam',
    'brand': 'Kissan',
    'quantity' : 3
}
cart.append(item)


# Mom asked me to add 2 whole chicken of Licious to the cart
item= {
    'name': 'Whole Chicken',
    'brand' : 'Licious',
    'quantity' : 3
}
cart.append(item)


# Mom asked me to add a 4 packet of Large chips of Lays
item = {
    'name' : 'Large Chips',
     'brand' : 'Lays',
     'quantity' : 4
}
cart.append(item)
print(cart)

# Mom asked what was the first item we added to the cart
print(cart[0]['name'])

# Mom asked what was the last item we added to the cart
print(cart[4]['brand'])

# another way to see the last  item
print(cart[-1]['name'])

# Mom asked how many items we added in the cart
print(len(cart))
 
#  Mom asked to replace the Whole Chicken with Whole Turkey and change quantity from 3 to 2
cart[3]['name'] = 'Whole Turkey'
cart[3]['quantity'] = 2
print(cart)

# Mom asked to replace the strawberry jam with Tomato sauce and change quantity from 3 to 1 
# another way to replace
item = {
    'name':'Tomato sauce',
    'brand': 'Chings',
    'quantity' : 1
}

cart[1] = item 
print(cart)


# Mom asked to replace the bread with the pizza bread "doubt"
cart[1]['name']= 'Pizza Bread'
print(cart)

# Mom asked how many items are there in the cart 
print(len(cart))

# Mom asked to remove the pizza bread from the cart "doubt"
cart.pop(1)
print(cart)

# Mom asked to remove the Whole Turkey from the cart "doubt"


# Mom asked to read out the first item detail
print (f'You have added {cart[0]['quantity']} {cart[0]['name']} of {cart[0]['brand']} to the cart')

# Mom asked to read out the second item detail 
print(f'You have added {cart[1]['quantity']} {cart[1]['name']} of {cart[1]['brand']} to the cart')



