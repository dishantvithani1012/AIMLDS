# example of for loop on dictionary 
india = {
    "Sanju Samson": 3,
    "Abhishek Sharma": 69,
    "Ishan Kishan": 37,
    "Shreyas Iyer": 1,
    "Tilak Varma": 28,
    "Naman Dhir": 10,
    "Nitish Kumar Reddy": 21,
    "Axar Patel": 20,
    "Arshdeep Singh": 11,
    "Prince Yadav": 13,
    "Mayank Yadav": 0
}

#sum 
sum = 0
for key in india:
    sum = sum + india[key]
print(sum)

#count no of players who score 0 runs 
count = 0
for player, runs in india.items():
    if runs == 0:
        count += 1
        print(player, "scored 0 runs")

print("Number of players who scored 0:", count)

#count no of players who score >50 runs 

count = 0
for player , runs in india.items():
    if runs >=50 :
        count +=1
        print(player,"scored more than 50 runs " )
print("Number of players who scored 50 :",count)

#count no of players who score <10 runs 

count = 0
for player , runs  in india.items():
    if runs <=10:
        count+=1
        print(player,"scored less than 10 runs")
print("Number of players who scored less than 10 :",count)