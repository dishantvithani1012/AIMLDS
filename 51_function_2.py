#function that without return value with argument

def printLetter(letter,times):
    print(letter*times)
    return None

#function that with return value without argument

def getPi():
    #local variable
    pi = 22/7
    return pi # thow value of pi

#function Exucution
printLetter('--',15)
print("Dishant Vithai")
printLetter("--",15)
print("Bhavnagar")
printLetter("--",15)

pi= getPi()
print("Value of pi ",round(pi,2))