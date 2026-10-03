'''
write a pogram to calculate annual income, Tax, Net income from given monthly income using below tax rule 
    annual income                           Tax Rate
    Above Rs. 24,00,000                     40%
    From Rs. 20,00,001 to Rs. 24,00,000	    30%
    From Rs. 16,00,001 to Rs. 20,00,000	    20%
    From Rs. 12,00,000 to Rs. 16,00,000	    10%
    below 12,00,000                          0%
'''

monthly_income = float(input("Enter the monthly income :"))

#annual
annual_income = monthly_income *12

#tax
tax=0

if annual_income <=1200000:
    tax =0
elif annual_income <=1600000:
    tax = annual_income * 0.10
elif annual_income <=2000000:
    tax = annual_income * 0.20
elif annual_income <=2400000:
    tax = annual_income * 0.30
else:
    tax= annual_income *0.40

net_income = annual_income - tax

print("Monthly Income Is :",monthly_income)
print("Annual Income Is :",annual_income)
print("Tax Is :",tax)
print("Net Income Is :",net_income)