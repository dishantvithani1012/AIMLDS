#Arbitrary Argument functions
#create function that return sum of all the values 
def getSum(*numbers): # means number is tuppe(Cannnot be chaged , read only)
    sum =0
    for num in numbers:
        print(num,end=" ")
        sum+=num
    print("")
    return sum # funtion is finished

sum = getSum(10,20,30)
print(f"Sum of values :{sum}")
sum = getSum()
print(f"sum of values = {sum}")
sum = getSum(10,20,30,100)
print(f"sum of values = {sum}")
sum = getSum(10,20,30,100,500,1000)
print(f"sum of values = {sum}")
sum = getSum(10,20,30,100,500,1000,25000)
print(f"sum of values = {sum}")
