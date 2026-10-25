# write a program to print a  to 10 using recursion
# 1 2 3 4 5 6 7 8 9 10

def printNum(num):
    if num<=10:
        print(num,end=" ")
        num+=1
        printNum(num)#recursion (when function call itself repeatedly untill some condition is evaluated as false it is called recursion)
        #print(f"num at the time of function ends {num}")

num =1
printNum(num)