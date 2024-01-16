#bubble sort
def bubble_sort(L):
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            L[i], L[i+1]=L[i+1],L[i]
    return L

#heap sort
def heapify(L): #find the maximum of the list and puts it in first place
    place=0
    maxi=L[0]
    for i,w in enumerate(L):
        if w>maxi:
            place=i
            maxi=L[0]
    L[0],L[place]=L[0],L[place]

def heap_sort(L):
    nb=len(L)
    end=nb
    heapify(L)
    while end>0:
        end=end-1
        L[end],L[0]=L[0],L[end]
        heapify(L)
    return L

print(heap_sort(["b","ab"]))