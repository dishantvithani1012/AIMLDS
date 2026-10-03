product ={'name':"Iphone 18 pro max ",'price':300000,"weight":250.34,"available":True}

print(product['name'])
print(product['weight'])
print(product['price'])

#update value 

product['price']=245000
print(product['price'])

product['company']="Apple"

print(product)

print(product['company'])

#delete key
del product ['available']

print(product)  