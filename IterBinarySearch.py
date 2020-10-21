#here is my binary search implementation of a sorted list 

data = [2,4,5,6,7,8,10,13,15,18,19,25,26,27,28,29,30,31,32,3]
target = 25

def binary_search(data, target):
   
    count = 0
    low = 0
    high = len(data) - 1
    
    while low <= high:
        FoundNum = "We found your Number {}, and it only took {} iterations".format(target,count)
        count += 1
        mid = (low + high) // 2

        if target == data[mid]:
            print(FoundNum)
            return True
            
        elif target < data[mid]:
            high = mid - 1
            print("high is:  {}".format(high))
        else:
            low = mid + 1
             
    print("We did not find {} in the list".format(target))       
    return False 

print("Result of iterated binary search of a sorted list: ")   
binary_search(data,target)
        


