data = [2,4,5,6,7,8,10,13,15,18,19,25,23,22]

target = 23

def linear_search(data, target):
    count = 0
    for i in range(len(data)):
        count +=1
        if data[i] == target:
            print("We found {} and it took only {} iterations".format(target,count))
    return False
          
linear_search(data, target)