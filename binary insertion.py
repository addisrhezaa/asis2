def binary(data, val, high, low):
    if high == low:
        if data[high] > val :
            return high
        else:
            return high + 1
    elif high > low:
        return high

    mid = (high + low) // 2
    if data[mid] < val :
        return binary(data, val, mid+1, low)
    elif data[mid] > val :
        return binary(data, val, high, mid-1)
    else :
        return mid

def binary_insertion(data):
    print(data)
    for i in range(1, len(data)):
        val = data[i]
        j = binary(data, val, 0, i-1)
        data = data[:j] + [val] + data[j:i] + data[i+1:]
        print(data)
    return data

binary_insertion([5,2,1,4,3])