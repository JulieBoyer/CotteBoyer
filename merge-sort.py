import sys
import time

def merge_sorted_sublists(b, begin, middle, end, a):
    # Merge two adjacent sub-lists inside the same array
    #
    # begin:  Start index, included.
    # middle: Start of second list, included.
    # end:    End index, excluded.
    # a:      The source list to sort.
    # b:      The destination list where to copy sorted items.

    # We iterate on both sub-lists at the same time, selecting each time the
    # lowest element.
    # We thus need two indices.
    i = begin  # Index on first sub-list.
    j = middle # Index on second sub-list.
    
    # Process all elements of both sub-lists
    for k in range(begin, end):
        
        # We choose current element (index i) of first sub-list
        if i < middle and (j >= end or a[i] <= a[j]):
            b[k] = a[i]
            i += 1

        # We choose current element (index j) of second sub-list
        else:
            b[k] = a[j]
            j += 1

def merge_sort(b, begin, end, a):
    # begin: Start index, included.
    # end:   End index, excluded.
    # a:     The source list to sort.
    # b:     The destination list where to copy sorted items.
    
    # One element
    if end - begin <= 1:
        return

    # Get middle index
    middle = (begin + end) // 2
    
    # Sort the two sub-lists from b into a
    merge_sort(a, begin, middle, b)
    merge_sort(a, middle, end, b)
    
    # Merge sorted sub-lists from a into b
    merge_sorted_sublists(b, begin, middle, end, a)

# Read standard input
words = sys.stdin.readlines()

# Remove new line character
words = [w.rstrip() for w in words]

# Remove empty words
words = list(filter(lambda s: s != '', words))

# Record start time
start_time = time.perf_counter()

# Make a copy of words' list
words2 = words.copy()

# Sort
merge_sort(words, 0, len(words), words2)

# Print sorted words
print("\n".join(words))

# Print elapsed time
sys.stderr.write("Elasped time: %f s\n" % (time.perf_counter() - start_time))
