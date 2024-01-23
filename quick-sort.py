import sys
import time
    
def partition(a, lo, hi):
    """Divide the array into two parts:
         Left part contains elements lower than value p
         Right part contains elements greater than value p
         Value p is between occupies the cell between the two parts.
         
         Value p can be any value of the array to partition.
    """

    # The pivot is the middle value we have to choose.
    # We choose the rightmost value, because, in case the array is already
    # sorted in ascending order, this will be the highest value, and nothing
    # will be moved in the array.
    # On the other hand, if the array is sorted in descending order we will have
    # to move all elements.
    pivot = a[hi]

    # Initialize the index to the latest element of the left part of the array:
    # the part of the small elements (i.e.: < pivot).
    i = lo - 1

    # We loop on all elements of the array minus 1:
    for j in range(lo, hi):

        # Must the current element be part of the small elements?
        if a[j] <= pivot:
            
            # OK, we increase the index of the last of the small elements
            # Index i is now equal index j, or is pointing to an element of the
            # right part (i.e.: big values).
            i += 1
            if i != j:
                # We move the current element into the left part
                # => we swap it with the element at index i which is a big value
                a[i], a[j] = a[j], a[i]
    
    # We move the index to the place where the pivot value (middle element) must
    # be
    i += 1
    
    # If we are not at the end of the array (the pivot value), we swap
    if i != hi:
        # Exchange the pivot value and the last value
        a[i], a[hi] = a[hi], a[i]
        
    return i

def quick_sort(a, lo, hi):
    
    # Nothing to do if indices are wrong
    if lo >= hi or lo < 0:
        return

    # Partition the array in two parts:
    #  * A middle value is at index p
    #  * All values smaller than the middle value are in the left part
    #  * All values bigger than the middle value are in the right part
    p = partition(a, lo, hi)
    
    # We sort the both parts
    quick_sort(a, lo,    p - 1) # Sorting of small values
    quick_sort(a, p + 1, hi)    # Sorting of big values

# Read standard input
words = sys.stdin.readlines()

# Remove new line characters
words = [w.rstrip() for w in words]

# Remove empty words
words = list(filter(lambda s: s != '', words))

# Record start time
start_time = time.perf_counter()

# Sort words
quick_sort(words, 0, len(words) - 1)

# Print sorted words
print("\n".join(words))

# Print elapsed time
sys.stderr.write("Elasped time: %f s\n" % (time.perf_counter() - start_time))
