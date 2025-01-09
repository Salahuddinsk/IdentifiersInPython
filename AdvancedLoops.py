# 
numbers = [ 1 , 2, 3 , 4 , 5 , 6 ,7 ]
for i in range(0,len(numbers)):
    if (numbers[i] == 3):
        print(numbers[i])
    else:
        print(f'not to print  {numbers[i]}')    

"""
Ye wala approach kaam to kar raha hai lekin 3 milne ke baad bhi isne looping continue kiya
isse hamara time and resources waste hua
"""

print('\n')
for i in range(0,len(numbers)):
    if (numbers[i] == 3):
        print(numbers[i])
        break
    else:
        print(f'not to print  {numbers[i]}')    

"""
break use karne se hame jaldi mil gaya number jo chahiye tha jisse hamara time bach gaya
break is only used when you want to get that specific item in short amount of time
break use karke hamne loop ko wahi rok diya jaha par hamari condition satisfied hogayi iss waja se hame baaki 
ke items par loop nahi kiya 
"""

# revise all the past codes and har code ke upar likho ki kya hora hai usme 

    

