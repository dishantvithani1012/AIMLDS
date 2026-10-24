#Example of filter function
numbers =[10,20,30,40,50,60,100,200,500,1000]

#get values >=100
filtered_list =filter(lambda num : num>=100,numbers)

print(list(filtered_list))