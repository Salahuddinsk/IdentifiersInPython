"""
Mom asked me to add some items to the cart
"""
#  Initially we have an empty cart
cart = []

# Mom told me to add a packet of milk in the empty cart
cart.append("Milk")

# Mom asked me again to add a bread
cart.append("bread")

# Mom asked me to add a jam
cart.append("Jam")

# Mom asked me to add chicken
cart.append("Chicken") 

# Mom asked me to add a packet of chips
cart.append("Chips")

print(cart)

# Mom asked what was the first item we added to the cart
print(cart[0])

# Mom asked what was the last item we added to the cart
print(cart[4])
# another way to see the last item
print(cart[-1])

# Mom asked how many items we added in the cart
print(len(cart))
 
#  Mom asked to replace the chicken with turkey
cart[3] ='turkey'
print(cart)

# Mom asked to replace the bread with the pizza bread
cart[1] = 'Pizza bread'
print(cart)

# Mom asked how many items are there in the cart
print(len(cart))

"""
len gives the total of the variable it will print in integers
"""

# Mom asked to remove the pizza bread from the cart
cart.pop(1)
print(cart)

# Mom asked to remove the turkey from the cart
cart.remove('turkey')
print(cart)

# pop- remove the item based on the index..
# remove - remove the item based on the value..

"""
'Pop' is faster compare to 'remove' function
'remove' function check every value till it finds the matching value, remember it should be 'Letter' , and
pop removes the item based on their index directly, remember it should be any 'number from 0 to 1 
"""
"""
append is basically a function which add value to the empty variable
"""

"""
assingment= create a similar story to show the add update and delete in the list
"""