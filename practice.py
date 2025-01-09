# print your name 5 times
for i in range (5):
    print('Shaikh Salahuddin')

# print table of 2
table = 2
for i in range (1,11):
    print(f'{table} * {i} = {table * i} ')

# print table of 3
table = 3
for i in range (1,11):
    print (f'{table} * {i} = {table * i}')

# print the table of 2 from 2 times of 5 till 2 times 10
table = 2
for i in range (5,21):
    print(f'{table} * {i} = {table * i}')

# print the table of 3 from 3 times 20 till 3 times 30
table = 3
for i in range (20,31):
    print (f'{table} * {i} = {table * i}')

# print the number from 1 to 10
for i in range (1,11):
    print(i)

# print the number from 6 till 20
for i in range (6,21):
    print (i)

# print the number from 1 to 10 by skipping one number in between example output = 1 3 5 7 9
for i in range (1,11,2):
    print(i)

# print the number from 5 to 20 by skipping four number in between
for i in range (5,21,5):
    print (i)

# print the number from 10 to 0 
for i in range (10,-1,-1):
    print(i)

# print the number starting from 20 till 15
for i in range (20,14):
    print(i)

# print the number strating from 10 till 0 by skipping 2 numbers in between
for i in range (10,-1,-3):
    print(i)

# make a list of groceries
cart = ['Onion','Watermelon','Banana','Papaya','apple','Carrot','Cucumber']
for i in range(0,len(cart)):
    print (cart[i])

#Print only watermelon onion and cucumber 
print('\n')
for i in range(0,len(cart)):
    if (cart[i] == 'Watermelon' ):
        print(cart[i])
    if (cart[i] == 'Onion'):
        print(cart[i])    
    if (cart[i] == 'Cucumber'):
        print(cart[i])

# Print the first item you get from the cart = watermelon onion and cucumber and then stop the loop
"""
break is used to stop the loop 
"""
print('\n')
for i in range(0,len(cart)):
    if (cart[i] == 'Watermelon' ):
        print(cart[i])
        break
    if (cart[i] == 'Onion'):
        print(cart[i])      
        break
    if (cart[i] == 'Cucumber'):
        print(cart[i])
        break
"""
 double equals is used for comparing the equality
 double equals check karne ke liye hota ki agar do item same hai 
"""


# Make a list of electronics devices (another way)
print('\n')
devices = ['Headphones','Microphones','Adapter','Plug Cable','Power Bank', 'Usb Cable']
for item in devices:
    print(item)



