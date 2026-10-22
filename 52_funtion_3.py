# defualt argument funtion 
def getSeconds(hours,minutes=0,seconds=0):
    print(f"Hours :{hours} Minutes :{minutes} Seconds :{seconds}")
    
    totalSeconds = (hours*60*60) +(minutes*60) + seconds
    
    return totalSeconds

result = getSeconds(10,9,35)
print(f"Total Seconds is :{result}")

result = getSeconds(10,9)
print(f"Total Seconds Is :{result}")

result = getSeconds(10)
print(f"Total Seconds Is : {result}")
