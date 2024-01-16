def bubble_sort(L):
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            l = L[i]
            L[i] = L[i+1]
            L[i+1] = l
    return L
