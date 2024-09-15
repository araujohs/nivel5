def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0,len(array) - i - 1):
            if(array[j]>array[j+1]):
                a = array[j]
                array[j] = array[j+1]
                array[j+1] = a
    return array

n = [218,303,232,198,998,451,346,668,190,694,601,629,834,565,39]
n = bubbleSort(n)
print(n)