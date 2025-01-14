"""
Assignment do append and print using 'f' string

"""

"""
Mom asked me to add some items to the cart
"""
#  Initially we have an empty cart
cart = []

# Mom told me to add 2 packet of milk from the brand of amul in the empty cart (isme dictionary used hai , isme hum kisi bhi chiz ya person ka pura data ya detail likh sakte hai , end me item append yani add hogaya hai cart me)
item = {
    'name' : 'Milk',
    'brand': 'Amul',
     'quantity': 2
}
cart.append(item)
print(cart)

# Mom asked me again to add 2 Packet of bread of Britannia to the cart  (isme dictionary used hai , isme hum kisi bhi chiz ya person ka pura data ya detail likh sakte hai , end me item append yani add hogaya hai cart me)
item = {
      'name': 'Bread',
      'brand': 'Britannia',
      'quantity': 2
}
cart.append(item)


# Mom asked me to add a 3 jar of Strawbery jams of Kissan to the cart (isme dictionary used hai , isme hum kisi bhi chiz ya person ka pura data ya detail likh sakte hai , end me item append yani add hogaya hai cart me)
item= {
    'name':'Strawberry jam',
    'brand': 'Kissan',
    'quantity' : 3
}
cart.append(item)


# Mom asked me to add 2 whole chicken of Licious to the cart (isme dictionary used hai , isme hum kisi bhi chiz ya person ka pura data ya detail likh sakte hai , end me item append yani add hogaya hai cart me)
item= {
    'name': 'Whole Chicken',
    'brand' : 'Licious',
    'quantity' : 3
}
cart.append(item)


# Mom asked me to add a 4 packet of Large chips of Lays (isme dictionary used hai , isme hum kisi bhi chiz ya person ka pura data ya detail likh sakte hai , end me item append yani add hogaya hai cart me)
item = {
    'name' : 'Large Chips',
     'brand' : 'Lays',
     'quantity' : 4
}
cart.append(item)
print(cart)

# Mom asked what was the first item we added to the cart (isme pehla item pata karne ke liye uska index used kiye hai aur item ka name tho dictionary me hai to uska key se naam mila hai )
print(cart[0]['name'])

# Mom asked what was the last item we added to the cart (isme akhri item pata karne ke liye uska index used kiye hai aur item ka name tho dictionary me hai to uska key se naam mila hai )
print(cart[4]['brand'])

# another way to see the last  item ( dusra tarika = isme akhri item pata karne ke liye uska index used kiye hai negative number used hai aur item ka name tho dictionary me hai to uska key se naam mila hai )
print(cart[-1]['name'])

# Mom asked how many items we added in the cart (isme total item kitna hai cart me wo malum padhra hai len use kar ke)
print(len(cart))
 
#  Mom asked to replace the Whole Chicken with Whole Turkey and change quantity from 3 to 2 
# isme key ki value change hori hai us item ka index use karke aur replace hoora hai dusre item se and same quantity bhi change hori hai index and key use kar ke
cart[3]['name'] = 'Whole Turkey'
cart[3]['quantity'] = 2
print(cart)

# Mom asked to replace the strawberry jam with Tomato sauce and change quantity from 3 to 1 
# another way to replace
# isme pura item ka value change kar rahe hai strawberry jam with tomato sauce se and quantity 3 to 1 end me cart ka index 
item = {
    'name':'Tomato sauce',
    'brand': 'Chings',
    'quantity' : 1
}

cart[2] = item 
print(cart)


# Mom asked to replace the bread with the pizza bread 
# isme key ki value change hori hai us item ka index use karke aur replace hoora hai dusre item se
cart[1]['name']= 'Pizza Bread'
print(cart)

# Mom asked how many items are there in the cart 
# (isme malum padhra hai cart me total kitne item hai len se hum pata kar sakte hai variable me total item kitne values hai)
print(len(cart))

# Mom asked to remove the pizza bread from the cart 
# (isme item cart se nikaal rahe hai ,pop function used hai , pop me index use hota hai)
cart.pop(1)
print(cart)

# Mom asked to remove the Whole Turkey from the cart "doubt"


# Mom asked to read out the first item detail
# isme f string use kiye hai f' ke baad jo bhi bracket me rahenge sab variable hojayenge or item ka key aur index daal rahe hai
# f string me output text me print hota hai 
print (f'You have added {cart[0]['quantity']} {cart[0]['name']} of {cart[0]['brand']} to the cart')

# Mom asked to read out the second item detail 
# isme f string use kiye hai f' ke baad jo bhi bracket me rahenge sab variable hojayenge or item ka key aur index daal rahe hai
# f string me output text me print hota hai 
print(f'You have added {cart[1]['quantity']} {cart[1]['name']} of {cart[1]['brand']} to the cart')

print('\n')

print(f'these are the items you have added in the cart')
print(f'{cart[0]['quantity']} {cart[0]['name']} of {cart[0]['brand']}')
print(f'{cart[1]['quantity']} {cart[1]['name']} of {cart[1]['brand']} ')
print(f'{cart[2]['quantity']} {cart[2]['name']} of {cart[2]['brand']}')
print(f'{cart[3]['quantity']} {cart[3]['name']} of {cart[3]['brand']}')

print('\n')
# another way to use for loop with f string
"""
niche wale loop me cart me jo bhi items hai sab print hora hai using for loop and f- string 
isme time kam lag raha hai aur chota code hai as compared upar wale se
"""

for i in range (0,len(cart)):
    print(f'{cart[i]['quantity']} {cart[i]['name']} of {cart[i]['brand']}')

print('\n')
# Update the Whole Turkey to the Chicken using for loop and if else
for i in range (0,len(cart)):
    if(cart[i]['name'] == 'Whole Turkey'):
        cart[i]['name'] = 'Chicken'
        print(f'{cart[i]['quantity']} {cart[i]['name']} of {cart[i]['brand']}')
        break
print('\n')

for i in range (0,len(cart)):
    print(f'{cart[i]['quantity']} {cart[i]['name']} of {cart[i]['brand']}')

# Update the brand of tomato sauce to kissan
print('\n')
for i in range(0,len(cart)):
    if(cart[i]['name'] == 'Tomato sauce'):
        cart[i]['brand'] = 'Kissan'
        print(f'{cart[1]['quantity']} {cart[1]['name']} of {cart[1]['brand']} ')

print('\n')
for i in range (0,len(cart)):
    print(f'{cart[i]['quantity']} {cart[i]['name']} of {cart[i]['brand']}')
