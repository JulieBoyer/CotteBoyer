#bubble sort
def bubble_sort(x):
    L=x.copy()
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            L[i], L[i+1]=L[i+1],L[i]
    return L

#heap sort
def heapify(L): #find the maximum of the list and puts it in first place
    if L==[]:
        return L
    place=0
    maxi=L[0]
    for i,w in enumerate(L):
        if w>maxi:
            place=i
            maxi=L[i]
    L[0],L[place]=L[place],L[0]

def heap_sort(L):
    a=L.copy()
    end=len(a)
    heapify(a)
    while end>0:
        end=end-1
        a[end],a[0]=a[0],a[end]
        heapify(a[0:end-1])
    return a

print(heap_sort(["ab","AB","cb","cde","CDE"]))