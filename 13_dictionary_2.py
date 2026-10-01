book ={} #will make emty dictionary

print(book)
#now adding new value

book['name']='The atomic habit'
book['price']=700
book['author']='james clear'

print(book)

#now adding tupple in dictionary

book['chapter']=(1,2,3,4,5)

print(book)

#adding list into dictionary

book['topics']=['index','introduction','habits','summary']

print(book['topics'])

print(book)

# adding topics in tupple
'''
book['topics'][0]= "beginig"
print(book)
'''

del book['chapter']
book['name']= "the power of habits"

print(book)

#print(book['name'])