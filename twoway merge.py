def merge(data, l, m, h):
    n1 = m - l + 1
    n2 = h - m
    L = [0] * n1
    H = [0] * n2
    for i in range(0, n1):
        L[i] = data[l + i]
    for j in range(0, n2):
        H[j] = data[m + j + 1]
 
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > H[j]:
            data[k] = H[j]
            j += 1
        else:
            data[k] = L[i]
            i += 1
        k += 1
 
    while i < n1:
        data[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        data[k] = H[j]
        j += 1
        k += 1

def twoway_merge(data):
    print(data)
    current_size = 1
    while current_size < len(data) - 1:
        low = 0
        while low < len(data)-1:
            mid = min((low + current_size - 1),(len(data)-1))
            high = ((2 * current_size + low - 1,len(data) - 1)
                    [2 * current_size
                    + low - 1 > len(data)-1])
            merge(data, low, mid, high)
            low = low + current_size*2
        current_size = 2 * current_size
        print(data)

twoway_merge([2,3,5,1,4,6])