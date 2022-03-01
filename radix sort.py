def counting(data, exp1): 
    
    length = len(data) 
    output = [0] * (length) 
    count = [0] * (10) 
    
    for i in range(0, length): 
        index = (data[i]/exp1) 
        count[int((index)%10)] += 1

    for i in range(1,10): 
        count[i] += count[i-1] 
    
    i = length-1
    while i>=0: 
        index = (data[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = data[i] 
        count[int((index)%10)] -= 1
        i -= 1
    for i in range(0,length): 
        data[i] = output[i] 

def radix_insertion(data):
    print(data)
    max1 = max(data)
    exp = 1
    while max1/exp > 0:
        counting(data,exp)
        exp *= 10
    print(data)
    
radix_insertion([2,3,5,1,4])