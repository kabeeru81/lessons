""" Submit 2nd March 2022 """

q1 = """
        My name is Jabir Bashir Kabir, 
        I am a shopkeeper at Usman Kasandrah stores.
        Please kindly help me create an empty shopping cart so that
        my customers can make purchases.
    """

# Write your answer below this line
print ('Kassandrah\n')

js_shoppingcart =[] 
print(f'Jabir, here is your cart:{js_shoppingcart}\n ')


Kabir Abubakar
shoppingcart =[]


q2 = """
        Thank you for the empty shopping cart,
        my customer james just came in and purchased
        cake, cashew, brownies and zobo. 
        Please kindly help him add them to the cart.
    """

# Write your answer below this line

js_shoppingcart.append('cake')
js_shoppingcart.append('cashew')
js_shoppingcart.append('brownies')
js_shoppingcart.append('zobo')
print(f'your cart conatins {js_shoppingcart}\n' )

Kabir Abubakar
shoppingcart.append('cake')
shoppingcart.append('cashew')
shoppingcart.append('brownies')
shoppingcart.insert(3,'zobo')
shoppingcart
['cake', 'cashew', 'brownies', 'zobo']


q3 = """
    James is happy with his purchase and wants to checkout.
    Please modify his cart so that it shows the price and quantity
    of each item purchased.
    """



# Write your answer below  this line

prices = [100, 200, 300, 400]
js_shoppingcart =['cake', 'cashew', 'brownies', 'zobo']
quantity = [2,3,4,5]

print(f'item 1 : {js_shoppingcart[0]}, the price is {prices[0]} and you got {quantity[0]} in total')
print(f'item 2 : {js_shoppingcart[1]}, the price is {prices[1]} and you got {quantity[1]} in total')
print(f'item 3 : {js_shoppingcart[2]}, the price is {prices[2]} and you got {quantity[2]} in total')
print(f'item 4 : {js_shoppingcart[3]}, the price is {prices[3]} and you got {quantity[3]} in total\n')

Kabir Abubakar
>>>shoppingcart1=[shoppingcart[0],'price is',prices[0],'and quantity is ',Quantity[0]]
>>> shoppingcart1
['cake', 'price is', 500, 'and quantity is ', 5]
>>> shoppingcart2=[shoppingcart[1],'price is',prices[1],'and quantity is ',Quantity[1]]
>>> shoppingcart2
['cashew', 'price is', 50, 'and quantity is ', 10]
>>> shoppingcart3=[shoppingcart[2],'price is',prices[2],'and quantity is ',Quantity[2]]
>>> shoppingcart3
['brownies', 'price is', 100, 'and quantity is ', 3]
>>> shoppingcart4=[shoppingcart[3],'price is',prices[3],'and quantity is ',Quantity[3]]
>>> shoppingcart4
['zobo', 'price is', 150, 'and quantity is ', 7]


q4 = """
    Thank you for all the help dear programmer,
    Please print the total to be paid by our dear customer
    and empty the cart one by one
    """

# Write your answer below this line

total_price =sum(prices)

total_quantity = sum(quantity)

print(f'the total items purchased is {total_quantity} and the price is {total_price} naira\n')

prices.clear()

quantity.clear()
js_shoppingcart.clear()

print(f'now your cart is empty and ready for the next operation Jabir: {js_shoppingcart},prices:{prices} and quantity: {quantity}\n')

Kabir Abubakar
>>> shoppingcart.clear()
>>> shoppingcart
[]
>>> prices.clear()
>>> prices
[]
>>> Quantity.clear()
>>> Quantity
[]

