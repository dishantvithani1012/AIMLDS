# write a program to print following pattern 
'''
*
* *
* * *
* * * *
* * * * *
'''
for astrik in range(0,6,1):
    for astrik in range(0,(astrik)):
        print("*",end=" ")
    print()