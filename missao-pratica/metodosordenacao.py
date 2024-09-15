def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0,len(array) - i - 1):
            if(array[j]>array[j+1]):
                a = array[j]
                array[j] = array[j+1]
                array[j+1] = a
    return array

def selectionSort(array):
    for i in range(len(array)):
        c = i
        for j in range(i+1,len(array)):
            if(array[c]>array[j]):
                c = j
        t = array[i]
        array[i] = array[c]
        array[c] = t

    return array