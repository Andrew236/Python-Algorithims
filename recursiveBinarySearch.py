#here is my implementation of a binary search of a sorted list recursively
 
data = [2,4,5,6,7,8,10,13,15,18,19,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
target = 25

def recursive_bin_search(data,target,low,high,count):
    
    if low > high:
        print("We did not find {}".format(target))
        return False
        
    else: 
        count += 1
        FoundNum = "We found your Number {}, and it only took {} iterations".format(target,count)
        mid = (low + high) // 2
        
        if target == data[mid]:
            print(FoundNum)
            return True 
        elif target < data[mid]:
            return recursive_bin_search(data, target, low, mid-1, count)
        else: 
            return recursive_bin_search(data,target,mid+1,high,count)
found = recursive_bin_search(data,target,0,len(data)-1,0)
if found == True:
    print('the element 25', found)
else:
    print("{} is not in the list".format(target))


