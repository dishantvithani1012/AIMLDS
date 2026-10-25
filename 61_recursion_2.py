'''
#Convert decimal number into binary

def binary(num):
    if num>0:
        remainder =num %2
        num=num//2
        binary(num)
        print(remainder,end="")

num =37
binary(num)
'''
#Convert decimal number into octal

def octal(num):
    if num>0:
        remainder = num %8
        num= num//8
        octal(num)
        print(remainder,end="")
num=14673
octal(num)
