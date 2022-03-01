def straight_insertion(data):
    length = len(data)
    print(data)
    
    for i in range(length):
        while i > 0:
            if data[i-1] > data[i]:
                print(data[i-1],data[i])
                temp = data[i]
                data[i] = data[i-1]
                data[i-1] = temp
                print(data)
            i -= 1
            
straight_insertion([5,2,1,4,3])
