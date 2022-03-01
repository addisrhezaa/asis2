def diminishing_increment(data):
    length = len(data)
    print(data)
    
    gap = length // 2 
    while gap > 0:
        for i in range(gap,length):
            anchor = data[i]
            j = i
            while j >= gap and data[j-gap] > anchor:
                data[j] = data[j-gap]
                j -= gap
            data[j] = anchor
            print(data)
        gap = gap // 2

diminishing_increment([5,2,1,4,3])       
