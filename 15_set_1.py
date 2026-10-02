fruits ={'apple','banana','mango','apple','kiwi'}
print(fruits)
fruits.add('water melon')
print(fruits)
fruits.add('grapes')
fruits.add("cherry")
fruits.add('grapes') # will not add
print(fruits)

fruits.remove('mango')
print(fruits)

set1 ={1,2,3,4,5}
set2 ={3,4,5,6,7}

union = set1.union(set2)
print(union)

intersection = set1.intersection(set2)
print(intersection)

difference = set1.difference(set2)
print(difference)

difference2 = set2.difference(set1)
print(difference2)

countries = ["India", "USA", "Canada", "UK", "Australia", "Germany", "India", "France", "Japan", "Brazil", "USA", "China", "Canada", "India", "Italy", "Germany", "Japan", "Australia", "India", "France"] #list contain duplicae values

# to remove convert to set then list

print(countries)

unique_contries = set(countries)
print(unique_contries)

#convert into list

countries=list(unique_contries)
countries.sort()
print(countries)