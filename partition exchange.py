def partition(data,low,high):
    i = (low-1)
    pivot = data[high]
    for j in range(low,high):
        if data[j] <= pivot:
            i += 1
            temp = data[i]
            data [i] = data[j]
            data[j] = temp
    temp = data[i+1]
    data [i+1] = data[high]
    data[high] = temp
    return (i+1)

def partition_exchange(data,low,high):
    print(data)
    if low < high:
        partindex = partition(data,low,high)
        partition_exchange(data,low,partindex - 1)
        partition_exchange(data,partindex + 1,high)

input = [2,3,5,1,4]
length = len(input)
partition_exchange(input,0,length-1)