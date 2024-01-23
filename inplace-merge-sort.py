import sys
import time

def merge_sorted_sublists_inplace(x, begin, middle, end):
    # Merge two adjacent sub-lists inside the same array
    #
    # x:      The source list to sort, in-place.
    # begin:  Start index, included.
    # middle: Start of second list, included.
    # end:    End index, excluded.

    # We iterate on both sub-lists at the same time, selecting each time the
    # lowest element.
    # We thus need two indices.
    i = begin  # Index on first sub-list.
    j = middle # Index on second sub-list.
    while i < middle and j < end:
    
        # ith element (first sub-list) is at right place
        if x[i] <= x[j]:
            i += 1
            
        # jth element (second sub-list) must be moved at ith position
        else:
            
            # Store value of jth element
            w = x[j]
            
            # Switch elements from position to position j - 1 to the right
            for k in range(j, i, -1):
                x[k] = x[k - 1]
                
            # Copy value of jth element at position i
            x[i] = w
            
            # Increment counters
            i += 1
            j += 1
            
            # The middle element has moved to the right
            middle += 1

def inplace_merge_sort(x, begin, end):
    # x:     The source list to sort in-place.
    # begin: Start index, included.
    # end:   End index, excluded.
    
    # One element
    if end - begin <= 1:
        return

    # Get middle index
    middle = (begin + end) // 2
    
    # Sort the two sub-lists from b into a
    inplace_merge_sort(x, begin, middle)
    inplace_merge_sort(x, middle, end)
    
    # Merge sorted sub-lists from a into b
    merge_sorted_sublists_inplace(x, begin, middle, end)

# Read standard input
words = sys.stdin.readlines()

# Remove new line character
words = [w.rstrip() for w in words]

# Remove empty words
words = list(filter(lambda s: s != '', words))

# Record start time
start_time = time.perf_counter()

inplace_merge_sort(words, 0, len(words))

# Print sorted words
print("\n".join(words))

# Print elapsed time
sys.stderr.write("Elasped time: %f s\n" % (time.perf_counter() - start_time))
