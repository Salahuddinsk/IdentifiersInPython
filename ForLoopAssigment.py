# print your name 5 times
for i in range (5):
    print('Shaikh Salahuddin')

# print table of 2
table = 2
for i in range (1,11):
    print (f'{table} * {i} = {table * i} ')

# print table of 3
table = 3
for i in range (1,11):
    print(f'{table} * {i} = {table * i}')

# print the table of 2 from 2 times of 5 till 2 times 10
table = 2
for i in range (5,11):
    print(f'{table} * {i} = {table * i}')

# print the table of 3 from 3 times 20 till 3 times 30
table = 3
for i in range (20,31):
    print(f'{table} * {i} = {table * i}')

# print the number from 1 to 10
for i in range (1,11):
    print(i)

# print the number from 6 till 20
for i in range (6,21):
    print(i)

# print the number from 1 to 10 by skipping one number in between example output = 1 3 5 7 9
for i in range (1,11,2):
    print(i) 

# print the number from 5 to 20 by skipping four number in between 
print('\n')
for i in range (5,21,5):
    print(i)    

# print the number from 10 to 0 
print('\n')
for i in range (10,-1,-1):
    print(i)

# print the number starting from 20 till 15
print('\n')
for i in range (20,14,-1):
    print(i)

# print the number strating from 10 till 0 by skipping 2 numbers in between
print('\n')
for i in range (10,-1,-3):
    print(i)

# make a list of groceries
print('\n')
cart = ['Cabbage' , 'Lettuce', 'Tomato','Carrot','Brinjal','Cucumber','Onion']
print(cart[0])
print(cart[1])
print(cart[2])
print(cart[3])
print(cart[4])
print(cart[5])
print(cart[6])

print('\n')
for i in range (0,len(cart)):
    print(cart[i])

# assingment do this forloop again by yourself