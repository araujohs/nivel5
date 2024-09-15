array = [218,303,232,198,998,451,346,668,190,694,601,629,834,565,39]

for i in range(len(array)):
    c = i
    for j in range(i+1,len(array)):
        if(array[c]>array[j]):
            c = j
    t = array[i]
    array[i] = array[c]
    array[c] = t

print(array)