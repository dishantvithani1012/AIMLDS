# example of user defined function
# def function-name(parameter/input):
#   line 1
#   line 2
#   return variable/None
#function create/define
#with return value with argument


#without return value without argument
def printLine():
    print("---"*5)
    
# with return value with argument
amount = int(input("Enter Amount :"))
rate = float(input("Enter Rate : "))
year = int(input("Enter Year : "))


printLine()
def getIntrest(amount,rate,year):
    intrest = (amount * rate * year ) / 100
    return intrest
printLine()



result = getIntrest(amount,rate,year)
print("Simple Intrest IS :",    result)