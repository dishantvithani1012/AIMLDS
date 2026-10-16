#example of for loop on tuple 
#findout sum and average of all values in tuple

tuple = (10,15,20,7,45,90,11,125)

sum =0
for item in tuple:
    print(item,end=' ')
    sum =sum + item
print()
print("Sum Is",sum)

average = sum / len(tuple)
print("Average is ",average)