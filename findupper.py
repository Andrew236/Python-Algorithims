#here is the code to find the upper case letters in a string iteratively and then recursively
#Recursively I only found the first upper case letter in the string. I am working on a way to find all 
#of the letters recursively

inputString = "lucidPRogramming"

def findUpperCase(inputString):
    count = 0
    for i in range (len(inputString)):
        if inputString[i].isupper():
            print (inputString[i])
            count +=1
    if count < 1:
        print("There was nothing in your list")
    
print("All upper case found iteratively in the string: ")    
findUpperCase(inputString)

def recursiveUpperCase(inputString, idx=0):
    
    if inputString[idx].isupper():
        return inputString[idx]
        
    if idx == len(inputString) - 1:
        return "No upper case found"
    return recursiveUpperCase(inputString,idx +1)
print("")
print("First upper case letter found in the string recursively is: ")
print(recursiveUpperCase(inputString))