"""
Mom asked me to add some items to the cart
"""
#  Initially we have an empty cart
cart = []

# Mom told me to add a packet of milk in the empty cart (isme milk cart variable me store hora hai ya to add hora hai)
cart.append("Milk")

# Mom asked me again to add a bread (isme bread cart variable me store hora hai ya to add hora hai)
cart.append("bread")

# Mom asked me to add a jam (isme jam cart variable me store hora hai ya to add hora hai)
cart.append("Jam")

# Mom asked me to add chicken (isme chicken cart variable me store hora hai ya to add hora hai)
cart.append("Chicken") 

# Mom asked me to add a packet of chips (isme packet of chips cart variable me store hora hai ya to add hora hai)
cart.append("Chips")

print(cart)

# Mom asked what was the first item we added to the cart (isme pehle item ka index daal ke malum padhra hai konsa pehla item daala hai)
print(cart[0])

# Mom asked what was the last item we added to the cart (isme akhri item ka index daal ke malum padhra hai konsa akhri item daala hai)
print(cart[4])

# another way to see the last item ( ye dusra tarika hai item find karne ka isme hum agar right se count karenge to negative number lena padega -1 to sabse last ka index -1 use kar sakte hai)
print(cart[-1])

# Mom asked how many items we added in the cart (isme malum padhra hai cart me total kitne item hai len se hum pata kar sakte hai variable me total item kitne hai)
print(len(cart))
 
#  Mom asked to replace the chicken with turkey (isme item adla badli hora hai us item ka index daal rahe hai or kisse change karna hai uska text daal rahe hai)
cart[3] ='turkey'
print(cart)

# Mom asked to replace the bread with the pizza bread (isme item adla badli hora hai us item ka index daal rahe hai or kisse change karna hai uska text daal rahe hai)
cart[1] = 'Pizza bread'
print(cart)

# Mom asked how many items are there in the cart  (isme malum padhra hai cart me total kitne item hai len se hum pata kar sakte hai variable me total item kitne values hai)
print(len(cart))

"""
len gives the total of the variable it will print in integers
"""

# Mom asked to remove the pizza bread from the cart (isme item cart se nikaal rahe hai ,pop function used hai , pop me index use hota hai)
cart.pop(1)
print(cart)

# Mom asked to remove the turkey from the cart (isme item cart se nikaal rahe hai , remove function used hai , remove me string matlab text use hota hai)
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