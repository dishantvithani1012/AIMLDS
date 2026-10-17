# write a program to print multiplication table of 30
'''
    30 X 1 = 30
    30 X 2 = 60
    30 X 3 = 90
    30 X 4 = 120
    30 X 5 = 150
    30 X 10 = 300
'''

number = 30
result =0

for multiplication in range(1,11):
    result = number * multiplication
    print(f"{number} X {multiplication :2}= {result:3}")