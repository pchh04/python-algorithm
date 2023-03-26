def bubblesort(nlist): # bubble sort
    for i in range(len(nlist), 1, -1):
        for j in range(i-1):
            if nlist[j] > nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
    return nlist

def insertionsort(nlist): # insertion sort
    for i in range(len(nlist)):
        for j in range(i, 0, -1):
            if nlist[j] >= nlist[j-1]:
                break
            else:
                nlist[j], nlist[j-1] = nlist[j-1], nlist[j]
    return nlist

def selectionsort(nlist): # selection sort
    for i in range(len(nlist)):
        x = nlist[i]
        for j in range(i, len(nlist)):
            if nlist[j] <= x:
                x = nlist[j]
                index = j
        nlist[i], nlist[index] = nlist[index], nlist[i]
    return nlist

def shellsort(nlist): # shell sort
    h = 1
    while (3*h + 1 < len(nlist)):
        h = 3*h + 1

    while (h > 0):
        for i in range(h, len(nlist)):
            temp = nlist[i]
            j = i
            while (nlist[j-h] > temp and j >= h):
                nlist[j] = nlist[j-h]
                j -= h
            nlist[j] = temp
        h = int(h/3)
    return nlist
