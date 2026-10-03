#write a program to findout profit or loss amount from given purchase and sales price of product
#task 
# also calculate and display profit or loss percentage 
#decide input 

purchase_price = float(input("Enter the purchase Price :"))
sales_price = float(input("Enter the Sales price :"))

#difference

difference = sales_price - purchase_price

if difference > 0:
    print(difference,"Is your profit")

if difference < 0:
    print(difference,"Is your loss")

print("Good Bye")
