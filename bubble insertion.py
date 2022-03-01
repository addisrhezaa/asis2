def bubble_insertion(data):
    length = len(data)
    print(data)

    i = 0
    while i < length:
        j = 0
        while j < length - 1:
            if data[j] > data[j+1]:
                print(data[j],data[j+1])
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
                print(data)
            j += 1
        i += 1
            
bubble_insertion([5,2,1,4,3])