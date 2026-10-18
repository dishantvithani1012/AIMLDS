# write a program to print following pattern 
'''
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
'''
'''
for i in range(5,0,-1):
    for j in range(0,i):
        print(j+1,end=" ")
    print()
'''

for i in range (5,0,-1):
    for j in range(0,i):
        print(j+1,end=' ')
    print()