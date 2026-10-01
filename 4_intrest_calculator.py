# simple intrest of given amount rate and year

amount= float(input("enter amount"))
rate = float(input("enter rate"))
year =  float(input("Enter year"))

#process

intrest =(amount * rate * year)/100

#round function
intrest=round(intrest,2)
print(f"Simple Intrest Is :{intrest}")